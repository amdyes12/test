#!/usr/bin/env python
#### encoding: utf-8

import RPi.GPIO
import time

PIN_DATA = 24
LED_A = 5
LED_B = 26
LED_C = 17
LED_D = 23
LED_E = 18
LED_F = 6
LED_G = 27
LED_DP = 4

DIGIT_1 = 21 
DIGIT_2 = 13
DIGIT_3 = 19
DIGIT_4 = 22
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)

RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)

RPi.GPIO.setup(DIGIT_1, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT_2, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT_3, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT_4, RPi.GPIO.OUT)

RPi.GPIO.output(DIGIT_1, True)
RPi.GPIO.output(DIGIT_2, True)
RPi.GPIO.output(DIGIT_3, True)
RPi.GPIO.output(DIGIT_4, True)

def showDigit(no, num, showDotPoint):
    RPi.GPIO.output(DIGIT_1, False)
    RPi.GPIO.output(DIGIT_2, False)
    RPi.GPIO.output(DIGIT_3, False)
    RPi.GPIO.output(DIGIT_4, False)

    if (num == 0) :
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,False)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,True)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 1):
        RPi.GPIO.output(LED_A,True)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,True)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,True)
        RPi.GPIO.output(LED_G,True)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 2):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,True)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,False)
        RPi.GPIO.output(LED_F,True)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 3):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,True)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 4):
        RPi.GPIO.output(LED_A,True)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,True)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 5):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,True)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 6):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,True)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,False)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 7):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,True)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,True)
        RPi.GPIO.output(LED_G,True)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 8):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,False)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    elif (num == 9):
        RPi.GPIO.output(LED_A,False)
        RPi.GPIO.output(LED_B,False)
        RPi.GPIO.output(LED_C,False)
        RPi.GPIO.output(LED_D,False)
        RPi.GPIO.output(LED_E,True)
        RPi.GPIO.output(LED_F,False)
        RPi.GPIO.output(LED_G,False)
        RPi.GPIO.output(LED_DP,not showDotPoint)

    if (no == 1):
        RPi.GPIO.output(DIGIT_1, True)
    elif (no == 2):
        RPi.GPIO.output(DIGIT_2, True)
    elif (no == 3):
        RPi.GPIO.output(DIGIT_3, True)
    elif (no == 4):
        RPi.GPIO.output(DIGIT_4, True)

try:
    t=0.003
    count = 0
    status = 0
    while True:
                status =1
                count +=1
                count %=2
                #time.sleep(0.3)
                RPi.GPIO.output(DIGIT_1, False)
                RPi.GPIO.output(DIGIT_2, False)
                RPi.GPIO.output(DIGIT_3, False)
                RPi.GPIO.output(DIGIT_4, False)
                print("count = ", count)
                '''
                showDigit(1,count ,False)
                time.sleep(t)
                showDigit(2,count ,False)
                time.sleep(t)
                showDigit(3,count ,False)
                time.sleep(t)
                showDigit(4,count ,False)
                time.sleep(t)
                '''
                if (count == 0):
                    showDigit(1, int(time.strftime("%M",time.localtime(time.time()))) / 10,False)
                    time.sleep(t)
                    showDigit(2, int(time.strftime("%M",time.localtime(time.time()))) % 10, True)
                    time.sleep(t)
                    showDigit(3, int(time.strftime("%S",time.localtime(time.time()))) / 10,False)
                    time.sleep(t)
                    showDigit(4, int(time.strftime("%S",time.localtime(time.time()))) % 10, True)
                    time.sleep(t)
                '''
                elif (count == 1):
                        time.sleep(t)
                        showDigit(1, int(time.strftime("%m",time.localtime(time.time()))) / 10,False)
                        time.sleep(t)
                        showDigit(2, int(time.strftime("%m",time.localtime(time.time()))) % 10, True)
                        time.sleep(t)
                        showDigit(3, int(time.strftime("%d",time.localtime(time.time()))) / 10,False)
                        time.sleep(t)
                        showDigit(4, int(time.strftime("%d",time.localtime(time.time()))) % 10, True)
                '''
except KeyboardInterrupt:
    pass
    '''
    RPi.GPIO.output(LED_A,True)
    RPi.GPIO.output(LED_B,False)
    RPi.GPIO.output(LED_C,False)
    RPi.GPIO.output(LED_D,True)
    RPi.GPIO.output(LED_E,True)
    RPi.GPIO.output(LED_F,True)
    RPi.GPIO.output(LED_G,True)
    RPi.GPIO.output(LED_DP,not showDotPoint)
    RPi.GPIO.output(DIGIT_1, True)
    '''
#showDigit(4,5,True)
#time.sleep(5)
print("hello")
RPi.GPIO.cleanup()
