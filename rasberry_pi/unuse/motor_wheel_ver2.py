
import time
import sys

import motor_arm

import wiringpi

def move(order, second):

    #左
    motor1_pin = 17 #前
    motor2_pin = 27 #後

    #右
    motor3_pin = 24 #前
    motor4_pin = 23 #後


    motor5_pin = 5
    motor6_pin = 6

    wiringpi.wiringPiSetupGpio() #PINの設定時最初にいるもの
    wiringpi.pinMode( motor1_pin, 1 ) #(PINの番号，PINのモード(output->1,input->0))
    wiringpi.pinMode( motor2_pin, 1 )
    wiringpi.pinMode( motor3_pin, 1 ) #(PINの番号，PINのモード(output->1,input->0))
    wiringpi.pinMode( motor4_pin, 1 )
    wiringpi.pinMode( motor5_pin, 1 ) #(PINの番号，PINのモード(output->1,input->0))
    wiringpi.pinMode( motor6_pin, 1 )
    time.sleep(0.3)

    if order == "go":
        if second == 0:
            print("goを止めるときはstop 0コマンド！")
        else:
            print(str(second)+"s,go")  
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 0 )
        
    elif order == "back":
        if second == 0:
            print("backを止めるときはstop 0コマンド！")
        else:
            print(str(second)+"s,go")  
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 0 )

    elif order == "right":
        if second == 0:
            print("右回転を止めるときはstop 0コマンド！")
        else:
            print(str(second)+"s,右回転")
        #GPIO.cleanup()
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )
        wiringpi.digitalWrite( motor3_pin, 0 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 1 )
    elif order == "left":
        if second == 0:
            print("左回転を止めるときはstop 0コマンド！")
        else:
            print(str(second)+"s,左回転")  
        #GPIO.cleanup()
        wiringpi.digitalWrite( motor1_pin, 0 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 1 )
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 0 )

    elif order == "right_only":
        if second == 0:
            print("right_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,right_only")
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 0 )

    elif order == "left_only":
        if second == 0:
            print("left_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,left_only")
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )

    elif order == "right_only_back":
        if second == 0:
            print("right_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,right_only")
        wiringpi.digitalWrite( motor3_pin, 0 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 1 )

    elif order == "left_only_back":
        if second == 0:
            print("left_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,left_only")
        wiringpi.digitalWrite( motor1_pin, 0 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 1 )

    elif order == "arm_only":
        if second == 0:
            print("arm_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,arm_only")
        wiringpi.digitalWrite( motor5_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor6_pin, 0 )

    elif order == "dan":
        if second == 0:
            print("left_onlyを止める時は 0コマンド！")
        else:
            print(str(second)+"s,only")
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 0 )
        wiringpi.digitalWrite( motor5_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor6_pin, 0 )


    time.sleep(second)

    # 第4引数が0の場合は、ブレーキをしない
    # 第3引数がbreakの場合は、ブレーキ
    if order == "stop" or second != 0:
        print("モーターstop")
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 1 )
        wiringpi.digitalWrite( motor3_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor4_pin, 1 )
        wiringpi.digitalWrite( motor5_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor6_pin, 1 )

    wiringpi.digitalWrite( motor1_pin, 0 )#HIGH->1,LOW->0
    wiringpi.digitalWrite( motor2_pin, 0 )
    wiringpi.digitalWrite( motor3_pin, 0 )#HIGH->1,LOW->0
    wiringpi.digitalWrite( motor4_pin, 0 )
    wiringpi.digitalWrite( motor5_pin, 0 )#HIGH->1,LOW->0
    wiringpi.digitalWrite( motor6_pin, 0 )
    