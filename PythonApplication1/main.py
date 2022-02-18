import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import notification
import time
from kivy.utils import platform


class mainMenu(Screen):
    pass

class robotFiles(Screen):
    pass

class controlApp(App):

	

    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainMenu(name='menu'))
        sm.add_widget(robotFiles(name='files'))
        self.startservice()
        return sm

    def viewFiles(self):
        notification.notify(title='notifyTest', message='isThisWorking?')

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

