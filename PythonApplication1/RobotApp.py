import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class mainMenu(Screen):
    pass

class robotFiles(Screen):
    pass

class controlApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainMenu(name='menu'))
        sm.add_widget(robotFiles(name='files'))

        return sm
 
kv = controlApp()
kv.run()

