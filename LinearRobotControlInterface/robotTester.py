import robot, Queue, time

q = Queue.Queue()
q.put("home")
q.put("terminate")
robot = robot.robot(q)
