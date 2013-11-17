import os
import threading
import subprocess

class Subprocess:

	exited = False
	
	def execute(self,popenArgs):
		def runInThread(self,popenArgs):
			FNULL = open(os.devnull, 'w')
			proc = subprocess.Popen(popenArgs, stdout=FNULL, stderr=subprocess.STDOUT)
			proc.wait()
        		self.exited = True
			return

		thread = threading.Thread(target=runInThread, args=(self,popenArgs))
		thread.start()
		# returns immediately after the thread starts
		return thread

	def hasExited(self):
		return self.exited
