import config, debug, serial, time

class linearRobotControl(object):
	#global variables
	instruction = ""
	response = None
	position = 0.0 

	"""
	LinearRobotControl contains all of the functions needed for 
	basic control of the linear phenotyping robot. Uses the pyserial
	library to control the arduino microcontroller by sending commands.

	Author: Carl Cortright-Gilroy Lab, Madison, Wisconsin
	Date: 7/5/2015
	"""
	def __init__(self):
		self.ser = serial.Serial(timeout=0)

	#moves the bot a certain distance 
	#returns false if that distance is out of bounds
	def move(self, length):
		#If the move goes out of bounds return false
		if (self.position + length <= 0) or (self.position + length >= config.length):
			return False
		else:
			#wait for the bot to receive the command
			while self.response != "Received\n":
				self.ser.write("m%f" % length)
				time.sleep(2)
				self.response = self.ser.readline()
			#set instruction and response vars and flush input buffer
			self.instruction = "m%f" % length
			self.response = None
			self.ser.flushInput()
			#wait for bot to finish move
			self.waitForBot()
			#set the new postion
			self.position += length
			#print debug info
			if debug.debug == True:
				print "Position: %f" % self.position
			return True

	#moves the bot to its home position
	def home(self):
		#waiting for the bot to receive the command
		while self.response != "Received\n":
				self.ser.write("home")
				time.sleep(2)
				self.response = self.ser.readline()
		#reset the instruction and response variables and flush the input buffer
		self.instruction = "home"
		self.response = None
		self.ser.flushInput()
		#wait until done moving
		self.waitForBot()

	#waits for the bot to respond with either 'home' or 'done'
	def waitForBot(self):
		#wait for the bot to respond 
		while (self.response != 'done\n') and (self.response != 'home\n'):
			time.sleep(2)
			self.response = self.ser.readline()
			#print debug info
			if debug.debug == True:
				print "Instruction: " + self.instruction
				print "Response: " + self.response
		#if the bot gets to home, set the postition to 0
		if self.response == "home\n":
			self.position = 0.0
			#debug info
			if debug.debug == True:
				print "Position: %f" % self.position
		#set instruction and response vars, flush input buffer
		self.response = None
		self.instruction = None
		self.ser.flushInput()

	#sets the port number
	def setPort(self, port):
		#shift port due to bug in pyserial
		config.port = port - 1
		self.ser.port = config.port
		#debug info
		if debug.debug == True:
			print "Port: %i" % self.ser.port

	#sets the baudrate
	def setBaud(self, baud):
		config.baud = baud
		self.ser.baudrate = config.baud
		if debug.debug == True:
			print "Baudrate: %i" % self.ser.baudrate

	#opens the serial connection after port and baud are set up
	def openConnection(self):
		self.ser.open()
		if debug.debug == True:
			print "T/F the port is open: %s" % self.ser.isOpen()
			
	#closes the serial connection
	def quit(self):
		self.ser.close()
