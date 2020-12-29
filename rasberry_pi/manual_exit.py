import time
import os

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
    
GPIO.setmode(GPIO.BCM)

GPIO.cleanup()

print("終了します．")

time.sleep(1)

os.system("sudo shutdown -h now")
