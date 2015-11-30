import linearRobot

robot = linearRobot.linearRobot(10)
robot.setLength(2000)
print robot.getLength()
print robot.getSpeed()
robot.printConfig()