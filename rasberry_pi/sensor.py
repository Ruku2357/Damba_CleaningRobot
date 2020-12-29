import time

import ultrasonic_sensor_1
import ultrasonic_sensor_2
import ultrasonic_sensor_3
import ultrasonic_sensor_4
import ultrasonic_sensor_5
import ultrasonic_sensor_6
import ultrasonic_sensor_7
import led

import RPi.GPIO as GPIO

order = 0
print("マニュアル操作開始")
print("1~7:センサー,0:終了")
def manual():
    while True:
        order = input("操作->")
        try:
            order = int(order)
        except:
            print("整数を入れてください．")
        
        if order == 1:#前進
            print(ultrasonic_sensor_1.reading(1))
            print("完了")

        if order == 2:#後退
            print(ultrasonic_sensor_2.reading(1))
            print("完了")

        if order == 3:#右折
            print(ultrasonic_sensor_3.reading(1))
            print("完了")

        if order == 4:#左折
            print(ultrasonic_sensor_4.reading(1))
            print("完了")

        if order == 5:#アームアップ?
            print(ultrasonic_sensor_5.reading(1))
            print("完了")

        if order == 6:#アームダウン?
            print(ultrasonic_sensor_6.reading(1))
            print("完了")

        if order == 7:#距離
            print(ultrasonic_sensor_7.reading(1))
            print("完了")

        if order == 0:#終了
            GPIO.cleanup()
            print("終了します．")
            break

    print("終了!!")

manual()
