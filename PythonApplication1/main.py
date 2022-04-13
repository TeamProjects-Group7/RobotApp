import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from plyer import notification
import time
from kivy.utils import platform
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import paramiko
from paho.mqtt import client as mqtt



class mainMenu(Screen):
	pass

class robotFiles(Screen):
	view = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		Clock.schedule_once(self.createScrollView)
		
	def createScrollView(self, dt):
		test = ["element {}".format(i) for i in range(40)]
		layout = GridLayout(cols=1, size_hint_y=None, row_default_height=200)
		layout.bind(minimum_height=layout.setter("height"))
		
		for element in test:
			layout.add_widget(Button(text=element))
		scrollview = ScrollView()
		scrollview.add_widget(layout)
		self.view.add_widget(scrollview)
	


class controlApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainMenu(name='menu'))
        sm.add_widget(robotFiles(name='files'))
        self.startservice()
        return sm
        
    def on_message(self, client, userdata, message):
    	incoming = str(message.payload.decode("utf-8"))
    	notification.notify(title='myService', message=str(incoming))
    	print("message received " ,str(message.payload.decode("utf-8")))
    	print("message topic=",message.topic)
    	print("message qos=",message.qos)
    	print("message retain flag=",message.retain)
	
    def on_connect(self, client, userdata, flags, rc):
    	if rc == 0:
    		notification.notify(title='myService', message='connected successfuly')
    	else:
    		notification.notify(title='myService', message='failed to connect')

    def setIdleOff(self):
    	client = mqtt.Client("newClient1")
    	broker_address = "broker.hivemq.com"
    	client.on_message=self.on_message
    	client.on_connect=self.on_connect
#client.username_pw_set(username="group7robot", password="thisisntsecureohwell")
    	client.connect(broker_address)
    	time.sleep(4)
    	client.publish("ROBOT_IDLE", "notidling")
	
    def setIdleOn(self):
    	client = mqtt.Client("newClient2")
    	broker_address = "broker.hivemq.com"
    	client.on_message=self.on_message
    	client.on_connect=self.on_connect
#client.username_pw_set(username="group7robot", password="thisisntsecureohwell")
    	client.connect(broker_address)
    	time.sleep(4)
    	client.publish("ROBOT_IDLE", "idling")

	
    def turnOffAlert(self):
    	client = mqtt.Client("newClient3")
    	broker_address = "broker.hivemq.com"
    	client.on_message=self.on_message
    	client.on_connect=self.on_connect
#client.username_pw_set(username="group7robot", password="thisisntsecureohwell")
    	client.connect(broker_address)
    	time.sleep(4)
    	client.publish("ROBOT_ALERT", "false")


    def viewFiles(self):
        ssh_client = paramiko.SSHClient()        
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
        	ssh_client.connect('10.16.22.87',username='pi',password='group7sp')

        	#stdin, stdout, stderr = ssh_client.exec_comm("cd ~/desktop")
        	stdin, stdout, stderr = ssh_client.exec_command("ls -a")
        	otherStuff = stdout.read().decode('ascii').strip("\n")
        	ssh_client.close()

        	notification.notify(title='notifyTest', message=otherStuff)
        except paramiko.AuthenticationException:
        	notification.notify(title='notifyTest', message='Auth')	
        except paramiko.SSHException:
        	notification.notify(title='notifyTest', message='SSH')
        except paramiko.BadHostKeyException:
        	notification.notify(title='notifyTest', message='BadHost')
        except:
        	notification.notify(title='notifyTest', message='NoIdea')
        


    def startservice(self, *args):
        if platform == "android":
            from jnius import autoclass
            service = autoclass('org.kivy.myapp.ServiceMyservice')
            self.mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(self.mActivity, '')
            

kv = controlApp()
kv.run()

