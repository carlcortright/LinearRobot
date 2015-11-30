import multiprocessing, Queue
import config, linearRobotControl
import time

def run(self):
	running = True
	print "In run!"
	while running:
		#gets the process command from the queue
		if self.queue.empty():
			command = None
		else:
			command = self.queue.get(timeout=0.01)
			print command
		#runs the appropriate process
		if command == "home":
			self.home()
		elif command == "test run":
			self.testRun()
		elif command == "start experiment":
			self.startExperiment()
		elif command == "terminate":
			self.terminate()
			running = False
		else:
			running = True

def startExperiment(self):
	print "StartExperiment called!"
def testRun(self):
	print "Test run called!"
def home(self):
	print "Home called!"
def move(self):
	print "Move called!"
def terminate(self):
	print "Terminate called!"


if __name__ == "__main__":
	q = Queue.Queue()
	robot = robot(q)
	q.put("home")
	q.put("terminate")
	robot.start()
	time.sleep(5)
