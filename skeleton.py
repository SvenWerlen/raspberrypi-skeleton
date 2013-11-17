import os
import random
import subprocess
from utils import *
from servolib import *
import RPi.GPIO as GPIO

"""Utility class to manipulate skeleton"""
class Skeleton:

	RED_LED=24
	SENSOR =17
	DELAY  =30

	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.RED_LED, GPIO.OUT)
		GPIO.setup(self.SENSOR, GPIO.IN)

	def __del__(self):
		GPIO.cleanup()

	def eyes(self,On=True):
		GPIO.output(self.RED_LED, On)

	def speak(self):
		# retrieve the list of available sounds
		snddir = os.path.dirname(os.path.realpath(__file__)) + "/sounds/"
		count = 0
		sounds = []
		for filename in os.listdir(snddir):
			if filename.endswith('.wav'):
				sounds.append(snddir + filename)
				count = count + 1
		# randomly pick one
		snd = random.randint(0,count-1)
		# play sound (asynchronously)
		p = Subprocess()
		p.execute(['aplay',sounds[snd]])
		# move jaw until sound is finished
		s = Servo(0,55,250)
		curAngle = -75
		while True:
			s.rotateSlowly(curAngle, 60)
			if p.hasExited():
				curAngle = 60
				break
			curAngle = - random.randint(0, 50)
			s.rotateSlowly(60, curAngle)
			if p.hasExited():
				break
		s.rotateSlowly(curAngle,-75)

	""" Detects and then illuminates and speaks """
	def automode(self):
		while True:
			if GPIO.input(self.SENSOR):
				self.eyes(True)
				self.speak()
				self.eyes(False)
				time.sleep(self.DELAY)
			time.sleep(0.5)
