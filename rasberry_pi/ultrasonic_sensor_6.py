import time

import RPi.GPIO as GPIO

def reading(sensor):
    
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BCM)
    TRIG = 19
    ECHO = 26

    miss_distance = -1
     
    if sensor == 1:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
         
        GPIO.output(TRIG, True)#超音波の送信
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
 
        while GPIO.input(ECHO) == 0: #ECHOがHIGHになってる
          signaloff = time.time()
         
        while GPIO.input(ECHO) == 1: #ECHOがLOWになった瞬間
          signalon = time.time()
 
        timepassed = signalon - signaloff #送信から受信の時間
        distance = timepassed * 340 * 100 / 2 #cm 
        
        if distance <= 300:
          #print("sensor1：" + str(distance) + "cm")
          return distance
        if distance > 300:
          GPIO.setup(TRIG,GPIO.OUT)
          GPIO.setup(ECHO,GPIO.IN)
          GPIO.output(TRIG, GPIO.LOW)
          time.sleep(0.3)
          
          GPIO.output(TRIG, True)#超音波の送信
          time.sleep(0.00001)
          GPIO.output(TRIG, False)
  
          while GPIO.input(ECHO) == 0: #ECHOがHIGHになってる
            signaloff = time.time()
          
          while GPIO.input(ECHO) == 1: #ECHOがLOWになった瞬間
            signalon = time.time()
  
          timepassed = signalon - signaloff #送信から受信の時間
          distance = timepassed * 340 * 100 / 2 #cm 
          if distance <= 300:
            #print("sensor1：" + str(distance) + "cm")
            return distance
          if distance > 300:
            #print("エラー6(300cmまで)")
            return miss_distance

    else:
        print("1でセンサー起動．")


