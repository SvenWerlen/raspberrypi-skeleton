from __future__ import division
import time

"""Utility class to manipulate servo"""
class Servo:
	
	# servo number
	servoNum = 0

	# min and max pulse (in ms) accepted by servo
	minMs = 0
	maxMs = 0
	# coefficients to compute pulse
	A = 0
	B = 0

	def __init__(self, servoNum, minMs, maxMs):
		self.minMs = minMs
		self.maxMs = maxMs
		
		# Formula: pulse =B - A * Angle
		# A = (max-min)/180
		# B = (min+max)/2
		
		self.A = (maxMs-minMs)/180
		self.B = (minMs+maxMs)/2

		self.servoNum = servoNum

	def __del__(self):
		# release servo
		self.sendPulse(0)

	def sendPulse(self,pulse):
		try:
			f = open("/dev/servoblaster", 'w')
			f.write("" + str(self.servoNum) + "=" + str(pulse) + "\n")
			f.close()
		except:
			print("Error writing to: " + str(self.servoNum) + " pulse: " + str(pulse))

	""" Immediate rotation to specified angle """
	def rotate(self,angle):
		# check that angle is between -90 and 90 degrees
		if angle < -90:
			angle = -90
		elif angle > 90:
			angle = 90

		pulse = int(round(self.B - self.A * angle))
		self.sendPulse(pulse)
	
	def log(self):
		print("Servo #" + str(self.servoNum) + " (" + str(self.minMs) + "," + str(self.maxMs) + ") => " + str(self.A) + ":" + str(self.B));

	""" Slow rotation (by 5 deg) """
	def rotateSlowly(self, fromAngle, toAngle):
		increment = 5 
		curAngle = fromAngle
		while True:
			self.rotate(curAngle)
			time.sleep(0.02)
			if fromAngle < toAngle:
				curAngle = curAngle + increment 
				if curAngle > toAngle:
					break
			else:
				curAngle = curAngle - increment
				if curAngle < toAngle:
					break

