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

    def viewFiles(self):
        notification.notify(title='notifyTest', message='isThisWorking?')
        ssh_client = paramiko.SSHClinet()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client_connect("192.168.0.186", 22, username="tw", password="Barbedone2#")
        stdin, stdout, stderr = ssh_client.exec_comm("ls ~/desktop")
        stdin, stdout, stderr = ssh_client.exec_comm("touch test")
        ssh_client.close()

    def startservice(self, *args):
        if platform == "android":
            from jnius import autoclass
            service = autoclass('org.kivy.myapp.ServiceMyservice')
            self.mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(self.mActivity, argument)
            print("service Started!")

kv = controlApp()
kv.run()

