import RPi.GPIO as GPIO
import time
import pygame;
# Import SPI library (for hardware SPI) and MCP3008 library.
GPIO.setmode(GPIO.BOARD)
servoPin1=11
GPIO.setwarnings(False)
GPIO.setup(servoPin1, GPIO.OUT)
pwm=GPIO.PWM(servoPin1, 50)
pwm.start(6)

servoPin2=12
GPIO.setwarnings(False)
GPIO.setup(servoPin2, GPIO.OUT)
rwm=GPIO.PWM(servoPin2, 50)
rwm.start(6)

ButtonPin=13
GPIO.setwarnings(False)
GPIO.setup(ButtonPin, GPIO.IN)

data_array=[]

from sys import exit;
pygame.mixer.init(48000, -16, 1, 1024);
sndA = pygame.mixer.Sound('D.wav');
sndB = pygame.mixer.Sound('E.wav');
sndC = pygame.mixer.Sound('F.wav');
sndD = pygame.mixer.Sound('G.wav');
soundChannelA = pygame.mixer.Channel(1);
soundChannelB = pygame.mixer.Channel(2);
soundChannelC = pygame.mixer.Channel(3);
soundChannelD = pygame.mixer.Channel(4);

import csv
with open('data.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		data_array.append( ', '.join(row))

print(data_array)
value=0
i=1
sound=False
while (value >= 0):
	if(GPIO.input(ButtonPin)==False and sound==False):
		sound=True
	elif(GPIO.input(ButtonPin)==False and sound==True):
		sound=False
	value = int(data_array[i])
	if (value<0):
		break

	elif (value<8000000 ):
		if(sound==True):
			soundChannelA.play(sndA);
                time.sleep(0.5);
		pwm.ChangeDutyCycle(2)
		time.sleep(1)
		pwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value<10000000):
		if(sound==True):
	                soundChannelB.play(sndB);
                time.sleep(0.5);
		pwm.ChangeDutyCycle(11)
		time.sleep(1)
		pwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value<12000000):
		if(sound==True):
	                soundChannelC.play(sndC);
                time.sleep(0.5);
		rwm.ChangeDutyCycle(11)
		time.sleep(1)
		rwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value>=12000000):
		if(sound==True):
	                soundChannelD.play(sndD);
                time.sleep(0.5);
		rwm.ChangeDutyCycle(2)
		time.sleep(1)
		rwm.ChangeDutyCycle(6)
		time.sleep(1)

	print(value)
	i=i+1
