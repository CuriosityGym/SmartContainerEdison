#! /usr/bin/python
import paho.mqtt.client as mqtt
import mraa
import time
from subprocess import call
import requests

b1= mraa.Gpio(6)  
b2 = mraa.Gpio(7)  
b1.dir(mraa.DIR_IN) 
b2.dir(mraa.DIR_IN)
isMQTTConnected=False

def notify():
	print("Interrupted")
	#client.publish("/CG/East/Alert", 1)
	#status = subprocess.call("iotkit-admin observation eastregionalert 1" , shell=True)
	#status = subprocess.call("iotkit-admin observation eastregionsupply 1" , shell=True)	
		



def on_connect(client, userdata, flags, rc):
    print("Connected to server. Connection code: "+str(rc))
    global isMQTTConnected	
    isMQTTConnected=True
    # Do a subscribe to "MQTTEdison" topic whenever a new connection is done 
#    client.publish("/CG/East/Alert", "1")
   #status = subprocess.call("iotkit-admin observation eastregionalert 1" , shell=True)
    #status = subprocess.call("iotkit-admin observation eastregionsupply 1" , shell=True)	
	
 #   client.subscribe("/CG/West/Alert", 1)



def readGPIO():
	#global lastState
	buttonState=b1.read() and  b2.read()
	print("B1: "+str(b1.read()))
	print("B2: "+str(b2.read()))
	if(buttonState==0 ):
		
		print ("Sending")	
		#lastState=buttonState
		client.publish("/CG/East/Alert", "1")
		#status = subprocess.call("iotkit-admin observation eastregionalert 1" , shell=True)
   		#status = subprocess.call("iotkit-admin observation eastregionsupply 1" , shell=True)	
		
	time.sleep(1)			
	

# Callback - called when a new message is received / published
def on_message(client, userdata, msg):
	#writes on console screen the topic and the message received
	print("Topico: "+msg.topic+" - Mensagem recebida: "+str(msg.payload))

#main program

def connected_to_internet(url='http://www.google.com/', timeout=25):
    try:
        _ = requests.get(url, timeout=timeout)
        print ("Yes")
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

connected_to_internet()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.loop_start()

while True:
	
	if isMQTTConnected:
		readGPIO()


