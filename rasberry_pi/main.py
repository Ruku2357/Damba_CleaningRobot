
import time
import threading
import sys
import os

import RPi.GPIO as GPIO

import motor_arm
import ultrasonic_sensor_1
import ultrasonic_sensor_2
import ultrasonic_sensor_3
import ultrasonic_sensor_4
import ultrasonic_sensor_5
import ultrasonic_sensor_6
import ultrasonic_sensor_7

#左キャタピラ
motor1_pin = 17 #前進
motor2_pin = 27 #後退

#右キャタピラ
motor3_pin = 24 #前進
motor4_pin = 23 #後退

#基本パラメータ
setting = 0 #ステータス
stairs = 0 #階段上
flag = False #mainのループ
stairs_time = 5 #階段から床への判断回数

setting_distance = 2 #稼働までの距離センサー１

#壁の対処パラメータ
out_distance = 10 #壁を検知する距離(cm)
go_back_time = 5 #壁に当たってから後退する時間(s)
turn_time = 10 #壁に当たった時の回避するための回転時間(s)左折
turn_time2 = 20 #壁に当たった時の回避するための回転時間(s)右折
wall_distance = 25 #壁か階段の距離(cm)(上の距離)(小さければ壁、大きければ階段)

#階段上り
step_turn_time = 2 #階段の回転(s)
difference_distance = 0.5 #右前と前の許容差
wall_d_distance = 3 #左右の調整時に近づきすぎの距離
back_wall_time = 3 #近づきすぎた時の後退時間

#階段下り
under_out_distance = 10 #下の距離がどのくらい空いたらダメか、床と階段の判断の距離
dis_dis_time = 0.5 #降るときの後退時の左右のセンサの時間の差

GPIO.setwarnings(False)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin,GPIO.OUT)
GPIO.setup(motor2_pin,GPIO.OUT)
GPIO.setup(motor3_pin,GPIO.OUT)
GPIO.setup(motor4_pin,GPIO.OUT)
time.sleep(0.3)

def play():

    stairs = 0 #階段上
    sett = 0
    print("前進")
    GPIO.output(motor1_pin, True)
    GPIO.output(motor2_pin, False)
    GPIO.output(motor3_pin, True)
    GPIO.output(motor4_pin, False)

    while flag:

        distance_sub1 = ultrasonic_sensor_1.reading(1)
        distance_sub2 = ultrasonic_sensor_2.reading(1)
        distance_sub3 = ultrasonic_sensor_3.reading(1)
        distance_sub4 = ultrasonic_sensor_4.reading(1)
        distance_sub5 = ultrasonic_sensor_5.reading(1)

        distance = {
            "top":distance_sub1,
            "right_under":distance_sub2,
            "right_front":distance_sub3,
            "left_under":distance_sub4,
            "left_front":distance_sub5
            }
        
        print(distance)

        if distance["right_front"] <= out_distance and distance["right_front"] != -1 and sett == 0 \
            or distance["left_front"] <= out_distance and distance["left_front"] != -1 and sett == 0:#前方に何かある
            
            print("壁検知")
            GPIO.output(motor1_pin, False)
            GPIO.output(motor2_pin, False)
            GPIO.output(motor3_pin, False)
            GPIO.output(motor4_pin, False)
            print("停止")
        
            if distance["top"] >= wall_distance and distance["top"] != -1:#階段

                print("上階段対処")

                while True:

                    distance_sub1 = ultrasonic_sensor_3.reading(1)
                    distance_sub2 = ultrasonic_sensor_5.reading(1)
                    distance["right_front"] = distance_sub1
                    distance["left_front"] = distance_sub2
                    
                    distance1 = distance["left_front"] - distance["right_front"]

                    print(str(distance_sub1) + ":" + str(distance_sub2) + ":" + str(distance1))
                    
                    if distance["right_front"] != -1 and distance["left_front"] != -1:
                        
                        if distance["left_front"] <= wall_d_distance:

                            print("近づきすぎバック")
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, True)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, True)
                            time.sleep(back_wall_time)
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, False)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, False)

                        if distance1 >= difference_distance:#右が前に出てる

                            print("右折")
                            GPIO.output(motor1_pin, True)
                            GPIO.output(motor2_pin, False)
                            #GPIO.output(motor3_pin, False)
                            #GPIO.output(motor4_pin, True)
                            time.sleep(step_turn_time)
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, False)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, False)
                            print("停止")

                        if distance1 * -1 >= difference_distance:#左が前に出てる

                            print("左折")
                            step_turn_time2 = step_turn_time + 1
                            #GPIO.output(motor1_pin, False)
                            #GPIO.output(motor2_pin, True)
                            GPIO.output(motor3_pin, True)
                            GPIO.output(motor4_pin, False)
                            time.sleep(step_turn_time2)
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, False)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, False)
                            print("停止")

                        if distance1 < difference_distance and distance1 * -1 < difference_distance:
                            break    
                    
                    time.sleep(0.1)

                print("前進")
                GPIO.output(motor1_pin, True)
                GPIO.output(motor2_pin, False)
                GPIO.output(motor3_pin, True)
                GPIO.output(motor4_pin, False)
                #前進

                print("上階段対処完了")
                stairs = 1
                sett = 1
            
            if distance["top"] < wall_distance and distance["top"] != -1 and sett == 0:#壁
                
                print("壁対処")
                print("バック")
                GPIO.output(motor1_pin, False)
                GPIO.output(motor2_pin, True)
                GPIO.output(motor3_pin, False)
                GPIO.output(motor4_pin, True)
                time.sleep(go_back_time)
                GPIO.output(motor1_pin, False)
                GPIO.output(motor2_pin, False)
                GPIO.output(motor3_pin, False)
                GPIO.output(motor4_pin, False)
                distance1 = distance["left_front"] - distance["right_front"]
                print(str(distance1))

                if distance1 > 0:#右が前に出てる

                    print("左折")
                    GPIO.output(motor1_pin, False)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, True)
                    GPIO.output(motor4_pin, False)
                    time.sleep(turn_time)
                    GPIO.output(motor1_pin, False)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, False)
                    GPIO.output(motor4_pin, False)
                    print("停止")

                if distance1 <= 0:#左が前に出てる

                    print("右折")
                    GPIO.output(motor1_pin, True)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, False)
                    GPIO.output(motor4_pin, False)
                    time.sleep(turn_time2)
                    GPIO.output(motor1_pin, False)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, False)
                    GPIO.output(motor4_pin, False)
                    print("停止")

                print("前進")
                GPIO.output(motor1_pin, True)
                GPIO.output(motor2_pin, False)
                GPIO.output(motor3_pin, True)
                GPIO.output(motor4_pin, False)
                print("壁対処完了")
                #前進
                sett = 1

        
        if distance["right_under"] >= under_out_distance and distance["right_under"] != -1 and sett == 0\
            or distance["left_under"] >= under_out_distance and distance["left_under"] != -1 and sett == 0:#下階段

            print("下階段検知")
            GPIO.output(motor1_pin, False)
            GPIO.output(motor2_pin, False)
            GPIO.output(motor3_pin, False)
            GPIO.output(motor4_pin, False)
            print("停止")

            print("下階段対処")

            ff2 = True
            dis_time = 0
            while ff2:
                distance_sub2 = ultrasonic_sensor_2.reading(1)#右
                distance_sub4 = ultrasonic_sensor_4.reading(1)#左

                if distance_sub2 <= under_out_distance and distance_sub2 != -1:#右
                    
                    print("右折")
                    GPIO.output(motor1_pin, True)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, False)
                    GPIO.output(motor4_pin, False)
                    ff3 = True
                    while ff3:
                        ff = True
                        distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                        if distance_sub4 >= under_out_distance and distance_sub4 != -1:#左
                            print("バック")
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, True)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, True)
                            while ff:
                                distance_sub2 = ultrasonic_sensor_2.reading(1)#右
                                distance_sub4 = ultrasonic_sensor_4.reading(1)#左

                                if distance_sub4 <= under_out_distance and distance_sub4 != -1:#左
                                    t = time.time()
                                    while ff:
                                        distance_sub2 = ultrasonic_sensor_2.reading(1)#右
                                        if distance_sub2 <= under_out_distance and distance_sub2 != -1:#右
                                            t2 = time.time()
                                            dis_time = t2 - t
                                            print("前進")
                                            GPIO.output(motor1_pin, True)
                                            GPIO.output(motor2_pin, False)
                                            GPIO.output(motor3_pin, True)
                                            GPIO.output(motor4_pin, False)
                                            while ff:
                                                distance_sub２ = ultrasonic_sensor_２.reading(1)#右
                                                if distance_sub２ >= under_out_distance and distance_sub２ != -1:#右
                                                    ff = False
                                                    print(dis_time)
                                                    print("停止")
                                                    GPIO.output(motor1_pin, False)
                                                    GPIO.output(motor2_pin, False)
                                                    GPIO.output(motor3_pin, False)
                                                    GPIO.output(motor4_pin, False)
                                                    ff3 = False
                                                time.sleep(0.1)
                                        time.sleep(0.1)
                                time.sleep(0.1)

                                if distance_sub2 <= under_out_distance and distance_sub2 != -1:#右
                                    t = time.time()
                                    while ff:
                                        distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                                        if distance_sub4 <= under_out_distance and distance_sub4 != -1:#左
                                            t2 = time.time()
                                            dis_time = t2 - t
                                            print("前進")
                                            GPIO.output(motor1_pin, True)
                                            GPIO.output(motor2_pin, False)
                                            GPIO.output(motor3_pin, True)
                                            GPIO.output(motor4_pin, False)
                                            while ff:
                                                distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                                                if distance_sub4 >= under_out_distance and distance_sub4 != -1:#左
                                                    ff = False
                                                    print(dis_time)
                                                    print("停止")
                                                    GPIO.output(motor1_pin, False)
                                                    GPIO.output(motor2_pin, False)
                                                    GPIO.output(motor3_pin, False)
                                                    GPIO.output(motor4_pin, False)
                                                    ff3 = False
                        time.sleep(0.1)

                if distance_sub4 <= under_out_distance and distance_sub4 != -1:#左
                    
                    print("左折")
                    GPIO.output(motor1_pin, False)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, True)
                    GPIO.output(motor4_pin, False)
                    ff3 = True
                    while ff3:
                        ff = True
                        distance_sub2 = ultrasonic_sensor_2.reading(1)#右1
                        if distance_sub2 >= under_out_distance and distance_sub2 != -1:
                            print("バック")
                            GPIO.output(motor1_pin, False)
                            GPIO.output(motor2_pin, True)
                            GPIO.output(motor3_pin, False)
                            GPIO.output(motor4_pin, True)
                            while ff:
                                distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                                distance_sub2 = ultrasonic_sensor_2.reading(1)#右1

                                if distance_sub2 <= under_out_distance and distance_sub2 != -1:#右1
                                    t = time.time()
                                    while ff:
                                        distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                                        if distance_sub4 <= under_out_distance and distance_sub4 != -1:#左
                                            t2 = time.time()
                                            dis_time = t2 - t
                                            print("前進")
                                            GPIO.output(motor1_pin, True)
                                            GPIO.output(motor2_pin, False)
                                            GPIO.output(motor3_pin, True)
                                            GPIO.output(motor4_pin, False)
                                            while ff:
                                                distance_sub4 = ultrasonic_sensor_4.reading(1)#左
                                                if distance_sub4>= under_out_distance and distance_sub4 != -1:#左
                                                    ff = False
                                                    print(dis_time)
                                                    print("停止")
                                                    GPIO.output(motor1_pin, False)
                                                    GPIO.output(motor2_pin, False)
                                                    GPIO.output(motor3_pin, False)
                                                    GPIO.output(motor4_pin, False)
                                                    ff3 = False
                                                time.sleep(0.1)
                                        time.sleep(0.1)
                                time.sleep(0.1)

                                if distance_sub4 <= under_out_distance and distance_sub4 != -1:#左
                                    t = time.time()
                                    while ff:
                                        distance_sub2 = ultrasonic_sensor_2.reading(1)#右1
                                        if distance_sub2 <= under_out_distance and distance_sub2 != -1:#右1
                                            t2 = time.time()
                                            dis_time = t2 - t
                                            print("前進")
                                            GPIO.output(motor1_pin, True)
                                            GPIO.output(motor2_pin, False)
                                            GPIO.output(motor3_pin, True)
                                            GPIO.output(motor4_pin, False)
                                            while ff:
                                                distance_sub2 = ultrasonic_sensor_2.reading(1)#右1
                                                if distance_sub2 >= under_out_distance and distance_sub2 != -1:#右1
                                                    ff = False
                                                    print(dis_time)
                                                    print("停止")
                                                    GPIO.output(motor1_pin, False)
                                                    GPIO.output(motor2_pin, False)
                                                    GPIO.output(motor3_pin, False)
                                                    GPIO.output(motor4_pin, False)
                                                    ff3 = False
                        time.sleep(0.1)

                    
                if dis_time > 0 and dis_time < dis_dis_time:
                    ff2 = False

                if dis_time  > 0 and dis_time * -1 < dis_dis_time:
                    ff2 = False
                
                time.sleep(0.1)

            GPIO.output(motor1_pin, False)
            GPIO.output(motor2_pin, False)
            GPIO.output(motor3_pin, False)
            GPIO.output(motor4_pin, False)
            print("停止")
            print("前進")
            GPIO.output(motor1_pin, True)
            GPIO.output(motor2_pin, False)
            GPIO.output(motor3_pin, True)
            GPIO.output(motor4_pin, False)
            #前進
            print("下階段対処完了")
            sett = 1
            stairs = 1

        if stairs == 1:
            print("階段通過中")
            t = 0
            while True:
                distance_stairs1 = ultrasonic_sensor_2.reading(1)
                distance_stairs2 = ultrasonic_sensor_4.reading(1)
                distance["right_under"] = distance_stairs1
                distance["left_under"] = distance_stairs2
                print(str(distance_stairs1) + ":" + str(distance_stairs2))

                if distance["right_under"] <= under_out_distance and distance["right_under"] != -1 \
                    and distance["left_under"] <= under_out_distance and distance["left_under"] != -1 :
                    
                    t = t + 1
                
                if t == stairs_time:
                    print("階段通過完了")
                    stairs = 0
                    break

                time.sleep(0.1)

        time.sleep(0.1)
        sett = 0
        print(sett)
        #print("end")

def controller():   

    global flag
    control = threading.Thread(target=play)
    control.setDaemon(True)
    while True:
        setting_d = ultrasonic_sensor_6.reading(1)

        if setting_d <= setting_distance:
            control.start()
            flag = True
            time.sleep(3)
            while True:
                setting_d = ultrasonic_sensor_6.reading(1)
                if setting_d <= setting_distance:
                    flag = False
                    GPIO.output(motor1_pin, False)
                    GPIO.output(motor2_pin, False)
                    GPIO.output(motor3_pin, False)
                    GPIO.output(motor4_pin, False)
                    GPIO.cleanup()
                    os.system("sudo shutdown -h now")
                time.sleep(0.5)
        time.sleep(0.5)

def no_controller():
    global flag
    flag = True
    play()

#controller()
no_controller()
