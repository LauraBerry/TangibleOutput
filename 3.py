import RPi.GPIO as GPIO
import time
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

data_array=[]

import csv
with open('data.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		data_array.append( ', '.join(row))

print(data_array)
value=0
i=1
while (value >= 0):
	value = int(data_array[i])
	if (value<0):
		break

	elif (value<8000000 ):
		pwm.ChangeDutyCycle(2)
		time.sleep(1)
		pwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value<10000000):
		pwm.ChangeDutyCycle(11)
		time.sleep(1)
		pwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value<12000000):
		rwm.ChangeDutyCycle(11)
		time.sleep(1)
		rwm.ChangeDutyCycle(6)
		time.sleep(1)

	elif (value>=12000000):
		rwm.ChangeDutyCycle(2)
		time.sleep(1)
		rwm.ChangeDutyCycle(6)
		time.sleep(1)

	print(value)
	i=i+1