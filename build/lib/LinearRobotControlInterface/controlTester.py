import linearRobotControl, debug

control = linearRobotControl.linearRobotControl()
debug.debug = True
control.setPort(16)
control.setBaud(9600)
control.openConnection()
control.home()
control.move(1)
control.home()
control.move(2)
control.move(-1)
control.quit()
print "Done."