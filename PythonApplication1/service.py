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
		notification.notify(title='myService', message='connected successfuly')
	else:
		notification.notify(title='myService', message='failed to connect')

#def idleSwitch(client):
#	if(connectedFlag == 1):
#		client.publish(Topic.ROBOT_IDLE, "false")
	

PythonService = autoclass('org.kivy.android.PythonService')



#PythonService.mService.setAutoRestartService(True)
#notification.notify(title='myService', message=str("Service Started"))
#client = mq.getClient()
#def on_message(client, userdata, msg):
#notification.notify(title='AlertStatus',message=str({msg.payload.decode()}))
#subscriber = mq.subscribe(on_message, Topic.ALERT_ON)
#mq.publish(client, 1, Topic.ALERT_ON)

client = mqtt.Client("my_client")
broker_address = "broker.hivemq.com"
client.on_message=on_message
client.on_connect=on_connect
#client.username_pw_set(username="group7robot", password="thisisntsecureohwell")
client.connect(broker_address)


client.subscribe([("ROBOT_IDLE", 0), ("ROBOT_ALERT", 0)])
time.sleep(4)
#client.publish("ROBOT_IDLE", "false")
client.loop_forever()
#Test Publishing
#for x in range(6):
#	client.publish("RobotTest", "Working")
#	time.sleep(3)
	
#notification.notify(title='myService', message=str("Service Ended"))
