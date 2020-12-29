import threading
import time
import sys
import os
import ultrasonic_sensor_6
import log_damba

def do():
    i = 0
    while True:
        print(i)
        i = i + 1
        time.sleep(1)

def dod():
    i = 10
    while True:
        print(i)
        i = i + 1
        time.sleep(1)
flag = False
setting_distance = 3
def controller():   

    control = threading.Thread(target=do)
    control.setDaemon(True)
    control1 = threading.Thread(target=do)
    control1.setDaemon(True)
    while True:
        setting_d = ultrasonic_sensor_6.reading(1)

        if setting_d <= setting_distance:
            control.start()
            flag = True
            print(str(flag))
            time.sleep(3)
            while True:
                setting_d = ultrasonic_sensor_6.reading(1)
                if setting_d <= setting_distance:
                    flag = False
                    print(str(flag))
                    control1.start()
                    time.sleep(10)
                    os.system("sudo shutdown -h now")
                time.sleep(0.5)
        time.sleep(0.5)

def damba():

    main = threading.Thread(target=do)
    main.setDaemon(True)

    while True:
        aa = ultrasonic_sensor_6.reading(1)
        print(aa)
        if aa < 4:
            main.start()
            time.sleep(10)
            os.system("sudo shutdown -h now")
            #sys.exit()

    setting = input("1:start order->")
    if setting == "1":
        main.start()
        time.sleep(10)
        sys.exit()

#controller()

log_damba.memo_write("aaaa")
