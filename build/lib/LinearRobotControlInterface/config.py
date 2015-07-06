"""
Configuration file for the linear robot. 
This file stores all relavant settings and writes
those settings to the config.txt. 
"""
speed = 0.0
port = 0
spacing = 10
length = 180
baud = 9600
cameraPort = 0
numPlants = 0
camera = "Cannon EOS5"
fileType = ".raw"

def printConfig():
	print "Speed: %f" % speed
	print "Port: %d" % port 
	print "Image Spacing: %f" % spacing
	print "Robot Length: %f" % length
	print "Camera Port: %d" % cameraPort
	print "Camera type: %s" % camera
	print "File type: %s" % fileType
def saveConfig():
	pass