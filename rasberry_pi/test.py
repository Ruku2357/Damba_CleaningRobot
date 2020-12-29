import threading
import time
import sys
import ultrasonic_sensor_6

def do():
    i = 0
    while True:
        print(i)
        i = i + 1
        time.sleep(1)

def damba():

    main = threading.Thread(target=do)
    main.setDaemon(True)

    while True:
        aa = ultrasonic_sensor_6.reading(1)
        if aa < 4:
            main.start()
            time.sleep(10)
            sys.exit()

    setting = input("1:start order->")
    if setting == "1":
        main.start()
        time.sleep(10)
        sys.exit()

damba()
