from jnius import autoclass
import time
from plyer import notification
from paho.mqtt import client as mqtt

#broker = 'broker.emqx.io'
#port = 1883
#username = 'group7robot'
#password = 'thisisntsecureohwell'

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


#PythonService.mService.setAutoRestartService(True)
print("service Started")
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
