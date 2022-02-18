from jnius import autoclass
import time
from plyer import notification


PythonService = autoclass('org.kivy.android.PythonService')
#PythonService.mService.setAutoRestartService(True)
print("service Started")

for x in range(6):
    notification.notify(title='myService', message=str("Testing"))
    time.sleep(3)
