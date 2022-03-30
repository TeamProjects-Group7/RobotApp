from jnius import autoclass
import time
from plyer import notification
from paho.mqtt import client as mqtt


def on_message(client, userdata, message):
	incoming = str(message.payload.decode("utf-8"))
	notification.notify(title='myService', message=str(incoming))
	print("message received " ,str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)
	
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		notification.notify(title='myService', message=str("connected successfuly"))
	else:
		notification.notify(title='myService', message=str("failed to connect"))
	

PythonService = autoclass('org.kivy.android.PythonService')


client = mqtt.Client("my_client")
broker_address = "broker.hivemq.com"
client.on_message=on_message
client.on_connect=on_connect
client.connect(broker_address)
client.loop_start()
#notification.notify(title='myService', message=str("Before Subscription"))
client.subscribe("RobotTest")
#client.publish("RobotTest", "Working")

#Test Publishing
#for x in range(6):
#	client.publish("RobotTest", "Working")
#	time.sleep(3)
	
time.sleep(4)
client.loop_stop()
#notification.notify(title='myService', message=str("Service Ended"))
