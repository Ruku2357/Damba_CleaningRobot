import time
import sys

import motor_arm
import motor_wheel as motor_wheel
import log_damba

import ultrasonic_sensor_1

def manual():
    while True:

        order = 0
        print("マニュアル操作開始")
        log_damba.memo_write("----------マニュアル操作開始-----------")
        print("1:前進\n2:後退\n3:右折\n4:左折\n5:腕右回転\n6:腕左回転\n11:右モータ\n12:右モータ逆\n21:左モータ\n22:左モータ逆\n0:終了")

        order = input("操作->")
        try:
            order = int(order)
        except:
            print("整数を入れてください．")
        
        if order == 1:#前進
            manual_second = input("秒数->")
            print("前進を" + manual_second + "秒間します．")
            log_damba.memo_write("前進を" + manual_second + "秒間します．")
            motor_wheel.move("go",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 2:#後退
            manual_second = input("秒数->")
            print("後退を" + manual_second + "秒間します．")
            log_damba.memo_write("後退を" + manual_second + "秒間します．")
            motor_wheel.move("back",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 3:#右折
            manual_second = input("秒数->")
            print("右折を" + manual_second + "秒間します．")
            log_damba.memo_write("右折を" + manual_second + "秒間します．")
            motor_wheel.move("right",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 4:#左折
            manual_second = input("秒数->")
            print("左折を" + manual_second + "秒間します．")
            log_damba.memo_write("左折を" + manual_second + "秒間します．")
            motor_wheel.move("left",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 5:#アームアップ?
            manual_second = input("秒数->")
            print("腕のモーターを" + manual_second + "秒間右回転します．")
            log_damba.memo_write("腕のモーターを" + manual_second + "秒間右回転します．")
            motor_arm.move("right",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 6:#アームダウン?
            manual_second = input("秒数->")
            print("腕のモーターを" + manual_second + "秒間左回転します．")
            log_damba.memo_write("腕のモーターを" + manual_second + "秒間左回転します．")
            motor_arm.move("left",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 11:#右のみ
            manual_second = input("秒数->")
            print("右のモーターを" + manual_second + "秒間回転します．")
            log_damba.memo_write("右のモーターを" + manual_second + "秒間回転します．")
            motor_wheel.move("right_only",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 12:#右のみ逆回転
            manual_second = input("秒数->")
            print("右のモーターを" + manual_second + "秒間逆回転します．")
            log_damba.memo_write("右のモーターを" + manual_second + "秒間逆回転します．")
            motor_wheel.move("right_only_back",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 21:#左のみ
            manual_second = input("秒数->")
            print("左のモーターを" + manual_second + "秒間回転します．")
            log_damba.memo_write("左のモーターを" + manual_second + "秒間回転します．")
            motor_wheel.move("left_only",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 22:#左のみ逆回転
            manual_second = input("秒数->")
            print("左のモーターを" + manual_second + "秒間逆回転します．")
            log_damba.memo_write("左のモーターを" + manual_second + "秒間逆回転します．")
            motor_wheel.move("left_only_back",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 30:#距離
            manual_second = input("秒数->")
            print("左のモーターを" + manual_second + "秒間逆回転します．")
            log_damba.memo_write("左のモーターを" + manual_second + "秒間逆回転します．")
            motor_wheel.move("arm_only",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 55:#だん
            manual_second = input("秒数->")
            print("モーターを" + manual_second + "秒間逆回転します．")
            log_damba.memo_write("モーターを" + manual_second + "秒間逆回転します．")
            motor_wheel.move("dan",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 56:#だん
            manual_second = input("秒数->")
            print("モーターを" + manual_second + "秒間逆回転します．")
            log_damba.memo_write("モーターを" + manual_second + "秒間逆回転します．")
            motor_wheel.move("dan2",float(manual_second))
            print("完了")
            log_damba.memo_write("完了")

        if order == 0:#終了
            motor_wheel.move("end",0)
            print("終了します．")
            log_damba.memo_write("完了")
            sys.exit()

        if order == 110:#終了
            motor_wheel.move("stop",0)
            print("終了します．")
            log_damba.memo_write("完了")

    print("終了!!")

manual()
