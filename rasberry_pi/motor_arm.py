import time
import sys

import wiringpi

def move(order, second):

    motor1_pin = 5
    motor2_pin = 6

    # GPIO出力モードを1に設定する
    wiringpi.wiringPiSetupGpio() #PINの設定時最初にいるもの
    wiringpi.pinMode( motor1_pin, 1 ) #(PINの番号，PINのモード(output->1,input->0))
    wiringpi.pinMode( motor2_pin, 1 )

    if order == "right":
        if second == 0:
            print("右回転を止めるときはstop 0コマンド！")
        else:
            print("モーター腕,"+str(second)+"s,右回転")
        wiringpi.digitalWrite( motor1_pin, 1 )#HIGH->1,LOW->0
        wiringpi.digitalWrite( motor2_pin, 0 )
        time.sleep(second)
    elif order == "left":
        if second == 0:
            print("左回転を止めるときはstop 0コマンド！")
        else:
            print("モーター腕,"+str(second)+"s,左回転")    
        wiringpi.digitalWrite( motor1_pin, 0 )
        wiringpi.digitalWrite( motor2_pin, 1 )
        time.sleep(second)

    # 第4引数が0の場合は、ブレーキをしない
    # 第3引数がbreakの場合は、ブレーキ
    if order == "stop" or second != 0:
        print("モーター腕,stop")
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 1 )

    time.sleep(1)

    wiringpi.digitalWrite( motor1_pin, 0 )
    wiringpi.digitalWrite( motor2_pin, 0 )
    
