#! /usr/bin/python
import paho.mqtt.client as mqtt
import mraa
import time
from subprocess import call

b1= mraa.Gpio(6)  
b2 = mraa.Gpio(7)  
b1.dir(mraa.DIR_IN) 
b2.dir(mraa.DIR_IN) 



def readGPIO():	
	buttonState=b1.read() or  b2.read()
	#print("B1: "+str(b1.read()))
	#print("B2: "+str(b2.read()))
	if(buttonState==1):
		
		print (buttonState)	
	#if(buttonState==0):
		
		#print (buttonState)	
	#time.sleep(1)
	


while True:
	readGPIO()




