import time

import RPi.GPIO as GPIO

def light(order):

    GPIO.setwarnings(False)
        
    GPIO.setmode(GPIO.BCM)
    Pin = 10 #GND 横のpin LEDの長い方

    GPIO.setup(Pin,GPIO.OUT)

    if order == 0:
        GPIO.output(Pin,0)
        print("LED_off")
    
    if order == 1:
        GPIO.output(Pin,1)
        print("LED_on")

def light_blinking(time):
    GPIO.setwarnings(False)
        
    GPIO.setmode(GPIO.BCM)
    Pin = 4

    GPIO.setup(Pin,GPIO.OUT)

    i = 0

    while i < int(time):

        GPIO.output(Pin,1)
        time.sleep(1)
        GPIO.output(Pin,0)
        time.sleep(1)

        i = i + 1

        print("LED"+str(time)+"回点灯しました．")


