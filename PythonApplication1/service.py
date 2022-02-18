from jnius import autoclass
import time
from plyer import notification


PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)
print("service Started")

while True:
    notification.notify(title='service', message=str("Testing"))
    time.sleep(3)