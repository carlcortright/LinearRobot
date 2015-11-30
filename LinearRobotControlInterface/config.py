"""
Configuration file for the linear robot. 
This file stores all relavant settings and writes
those settings to the config.txt. 
"""
#local variables to store configuration for easy access
speed = 0.0
port = 0
length = 180
baud = 9600
numPlants = 0
cameraPort = 0
camera = "Cannon EOS5"
fileType = ".raw"



#prints the current configuration
def printConfig():
	print "Speed: %f" % speed
	print "Port: %d" % port 
	print "Robot Length: %f" % length
	print "Baud Rate: %d" % baud
	print "Number of Plants: %d" % numPlants
	print "Camera Port: %d" % cameraPort
	print "Camera type: %s" % camera
	print "File type: %s" % fileType
#reads the saved configuration from the text file config.txt
def readConfig():
	global speed
	global port 
	global length
	global baud
	global numPlants
	global cameraPort
	global camera
	global fileType
	f = open("config.txt", 'r+')
	speed = float(f.readline()[:-1])
	port = int(f.readline()[:-1])
	length = float(f.readline()[:-1])
	baud = int(f.readline()[:-1])
	numPlants = int(f.readline()[:-1])
	cameraPort = int(f.readline()[:-1])
	camera = f.readline()[:-1]
	fileType = f.readline()[:-1]
	f.close()
#saves the current configuration to the the text file config.txt
def writeConfig():
	f = open("config.txt", 'r+')
	f.write(str(speed) + "\n")
	f.write(str(port) + "\n")
	f.write(str(length) + "\n")
	f.write(str(baud) + "\n")
	f.write(str(numPlants) + "\n")
	f.write(str(cameraPort) + "\n")
	f.write(camera + "\n")
	f.write(fileType  + "\n")
	f.close()

readConfig()