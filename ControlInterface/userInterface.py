from Tkinter import *
import tkFileDialog
import linearRobotControl
import config, debug
import sys, os, time


class linearRobotInterface:

	"""
	Tkinter implementation of the user interface for the Gilroy Lab 
	linear phenotyping robot.

	Author: Carl Cortright- Gilroy Lab, Madison, Wisconsin
	Date: 7/5/2015
	"""
	def __init__(self, master):
		#default settings
		master.protocol('WM_DELETE_WINDOW', self.destroy)
		#useful global variales 
		self.width = master.winfo_screenwidth()
		self.height = master.winfo_screenheight()
		self.master = master
		self.frame = Frame(master)
		self.directory = None

		#Set up the serial connection
		self.control = linearRobotControl.linearRobotControl()

		#change the title and icon
		master.wm_title("Gilroy Lab Robot Control Interface")
		master.iconbitmap('plantIcon.ico')

		#generate the user interface with two framed sections, one for the top and one for the bottom. 
		self.makeMenu(master)
		self.top = Frame(master=master, height=self.height/4, width=self.width/2-20)
		self.top.pack()
		self.bottom = Frame(master=master, height=self.height/4, width=self.width/2-20)
		self.createBottomButtons(self.bottom)

	"""makes the menu items"""
	def makeMenu(self, master):
		menu = Menu(master)
		master.config(menu=menu)
		filemenu = Menu(menu, tearoff=False)
		helpmenu = Menu(menu, tearoff=False)
		menu.add_cascade(label="file", menu=filemenu)
		menu.add_command(label="settings", command=self.settings)
		menu.add_command(label="camera options", command=self.camera_options)
		menu.add_cascade(label="help", menu=helpmenu)
		filemenu.add_command(label="new experiment", command=self.new_experiment)
		filemenu.add_separator()
		filemenu.add_command(label="exit", command=self.destroy)
		helpmenu.add_command(label="user manual", command=self.user_manual)
		helpmenu.add_command(label="about", command=self.about)
	"""creates the main robot control buttons at the bottom of the screen"""
	def createBottomButtons(self, bottom):
		bottom.pack()
		test_run = Button(master=bottom, text="test run", command=self.test_run, font=("Helvedica", 16))
		test_run.grid(in_=self.bottom, row=5, column=1)
		numplants_label = Label(master=bottom, text="Number of Plants:", font=("Helvedica", 16))
		numplants_label.grid(in_=self.bottom, row=5, column=2)
		numplants = Entry(master=bottom, font=("Helvedica", 16))
		numplants.grid(in_=self.bottom, row=5, column=3)
		setnum = Button(master=bottom, text="Set", command=lambda: self.add_plant_spots(self.top, numplants.get()), font=("Helvedica", 16))
		setnum.grid(in_=self.bottom, row=5, column=4, sticky="W")
		experiment_length_label = Label(master=bottom, text="Experiment Length(hours): ", font=("Helvedica", 16))
		experiment_length_label.grid(in_=self.bottom, row=6, column=1, columnspan=2, sticky="W")
		experiment_length_entry = Entry(master=bottom, font=("Helvedica", 16))
		experiment_length_entry.grid(in_=self.bottom, row=6, column=3, sticky="W")
		time_between_label = Label(master=bottom, text="Time Between Runs(mins): ", font=("Helvedica", 16))
		time_between_label.grid(in_=self.bottom, row=7, column=1, columnspan=2, sticky="W")
		time_between_entry = Entry(master=bottom, font=("Helvedica", 16))
		time_between_entry.grid(in_=self.bottom, row=7, column=3, sticky="W")
		start = Button(master=bottom, text="Start Experiment", font=("Helvedica", 16), command=self.start_experiment)
		start.grid(in_=self.bottom, row=8, column=1)
		stop = Button(master=bottom, text="Stop Experiment", font=("Helvedica", 16), command=self.stop_experiment)
		stop.grid(row=8, column=2)
	"""when the user changes the number of plants this method changes the layout of the interface"""
	def add_plant_spots(self, master, numplants):
		for entry in self.top.grid_slaves():
			entry.grid_forget()
		try:
			numplants = int(numplants)
			config.numPlants = numplants
		except ValueError:
			errorLabel = Label(master=self.top, font=('Helvedica', 16), text='Please enter a number.')
			errorLabel.pack()
			return
		for entry in self.top.slaves():
			entry.forget()
		for plantnum in range(1,numplants+1):
			nameLabel = Label(master=master, text="Name:", font=("Helvedica", 16))
			nameLabel.grid(row=0, column=plantnum)
			plantName = Entry(master=master, font=("Helvedica", 16))
			plantName.grid(row=1, column=plantnum)
			plantImage = PhotoImage(file="plant.gif")
			picture = Label(master=master, height=self.height/4, width=self.width/numplants, image=plantImage)
			picture.image = plantImage
			picture.grid(row=2, column=plantnum)
			onoffbutton = Checkbutton(master=self.top, text="Turn Off", font=("Helvedica", 16))
			onoffbutton.grid(row=3, column=plantnum)
	"""creates a new experiment in a specific directory"""
	def new_experiment(self):
		self.directory = tkFileDialog.askdirectory(title="Choose a folder to save the experiment in:")
	"""Changes the robot's configuration settings"""
	def settings(self):
		self.toplevel = Toplevel()
		self.toplevel.iconbitmap('plantIcon.ico')
		self.toplevel.title("Robot Settings")
		velocity_label = Label(master=self.toplevel, text="Speed(in cm/s):", font=("Helvedica", 16))
		velocity_label.grid(row=1, column=1)
		self.velocity_input = Entry(master=self.toplevel, font=("Helvedica", 16))
		self.velocity_input.grid(row=1, column=2)
		length_label = Label(master=self.toplevel, text="Robot Length(in cm):", font=("Helvedica", 16))
		length_label.grid(row=2, column=1)
		self.length_entry = Entry(master=self.toplevel, font=("Helvedica", 16))
		self.length_entry.grid(row=2, column=2)
		self.port_label = Label(master=self.toplevel, font=("Helvedica", 16), text="Port(e.g. 10 for COM10):")
		self.port_label.grid(row=3, column=1)
		self.port_entry = Entry(master=self.toplevel, font=("Helvedica", 16))
		self.port_entry.grid(row=3, column=2)
		self.baud_label = Label(master=self.toplevel, font=("Helvedica", 16), text="Baudrate(e.g. 9600):")
		self.baud_label.grid(row=4, column=1)
		self.baud_entry = Entry(master=self.toplevel, font=("Helvedica", 16))
		self.baud_entry.grid(row=4, column=2)
		save_button = Button(master=self.toplevel, text="save", font=("Helvedica", 16), command=self.savesettings)
		save_button.grid(row=5, column=1)
		exit_button = Button(master=self.toplevel, text="exit", font=("Helvedica", 16), command=self.exitsettings)
		exit_button.grid(row=5, column=2)
	"""Saves the entered settings in the config file."""
	def savesettings(self):
		try:
			#set the config vars
			config.length = float(self.length_entry.get())
			config.speed = float(self.velocity_input.get())
			#connect with robot
			self.control.setPort(int(self.port_entry.get()))
			self.control.setBaud(int(self.baud_entry.get()))
			self.control.openConnection()
		except ValueError:
			top = Toplevel()
			top.iconbitmap('plantIcon.ico')
			top.title("Error...")
			msg = Message(master=top, text="Error! Please enter only numbers!")
			msg.pack()
		finally:
			if debug.debug:
				config.printConfig()
			config.saveConfig()
			self.toplevel.destroy()
	"""Destroys the current top level settings window."""
	def exitsettings(self):
		self.toplevel.destroy()
	"""Displays the camera options menu when the menu item is clicked."""
	def camera_options(self):
		self.toplevel = Toplevel()
		self.toplevel.iconbitmap('plantIcon.ico')
		self.toplevel.title("Camera Settings")
		self.camera_port_label = Label(master=self.toplevel, text="Camera Port(e.g. 9 for COM9):", font=("Helvedica", 16))
		self.camera_port_label.grid(row=1, column=1)
		self.camera_port_entry = Entry(master=self.toplevel, font=("Helvedica", 16))
		self.camera_port_entry.grid(row=1, column=2)
		camera_select_label = Label(master=self.toplevel, font=("Helvedica", 16), text="Select your camera:")
		camera_select_label.grid(row=2, column=1)
		self.variable1 = StringVar(self.toplevel)
		self.variable1.set("Cannon EOS5")
		self.camera_select = OptionMenu(self.toplevel, self.variable1, "Cannon EOS5")
		self.camera_select.grid(row=2, column=2)
		file_type_label = Label(master=self.toplevel, font=("Helvedica", 16), text="Select your perfered file type:")
		file_type_label.grid(row=3, column=1)
		self.variable2 = StringVar(self.toplevel)
		self.variable2.set(".raw")
		self.file_type_entry = OptionMenu(self.toplevel, self.variable2, ".raw", ".jpeg", ".png")
		self.file_type_entry.grid(row=3, column=2)
		self.camera_option_save = Button(master=self.toplevel, font=("Helvedica", 16), text="save", command=self.save_camera_options)
		self.camera_option_save.grid(row=4, column=1)
		self.camera_option_exit = Button(master=self.toplevel, font=("Helvedica", 16), text="exit", command=self.exit_camera_settings)
		self.camera_option_exit.grid(row=4, column=2)
	"""Saves the camera options in the config file."""
	def save_camera_options(self):
		try:
			config.camera_port = int(self.camera_port_entry.get())
			config.camera = self.variable1.get()
			config.file_type = self.variable2.get()
		except ValueError:
			top = Toplevel()
			top.iconbitmap('plantIcon.ico')
			top.title("Error...")
			msg = Message(master=top, text="Error! Please enter only numbers!")
			msg.pack()
		finally:
			if self.control.debug:
				config.printConfig()
			config.saveConfig()
	"""Destroys the toplevel widget containing the camera options."""
	def exit_camera_settings(self):
		self.toplevel.destroy()
	"""Opens the user manual."""
	def user_manual(self):
		try:
			os.system("start usermanual.pdf")
			os.system("open usermanual.pdf")
		finally:
			if self.control.debug:
				print "User Manual opened. Check for error ^."
	"""Displays a popup with relavent production info"""
	def about(self):
		message = "Linear Robot control software v 0.9.\n\nCreated by Carl Cortright in association with Gilroy Lab, working under Dr. Simon Gilroy and Dr. Richard Barker. \n \n Contact: ckcortright@gmail.com"
		top = Toplevel(height=400, width=900)
		top.iconbitmap('plantIcon.ico')
		top.title("About")
		msg = Message(master=top, text=message)
		msg.pack()
	"""runs a test run so that the researcher can see the position of the plants in each picture"""
	def test_run(self):
		self.control.home()
		halfMoveLength = config.length/(config.numPlants*2)
		self.control.move(halfMoveLength)
		time.sleep(5)
		for plant in range(1, config.numPlants):
			self.control.move(halfMoveLength*2)
			time.sleep(5)
		self.control.home()
	"""Ends the experiment before the time is up."""
	def stop_experiment(self):
		pass
	"""Starts the experiment once everything is configured."""
	def start_experiment(self):
		if self.directory == None or self.directory == "":
			top = Toplevel()
			top.iconbitmap('plantIcon.ico')
			top.title("Error...")
			msg = Message(master=top, text="Error! Please choose a location to save the experiment(file->new experiment).")
			msg.pack()
			return
		else:
			pass
	def destroy(self):
		self.control.quit()
		self.frame.quit()
#Initialize the frame. 
root = Tk()
robot = linearRobotInterface(root)
root.mainloop()