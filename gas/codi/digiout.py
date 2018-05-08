#!/usr/bin/python
# -*- coding: utf-8 -*-
#digiout.py

import time
import RPi.GPIO as GPIO
import dweepy

# Sistema de detecció de fum
#HARDWARE SETUP
# P1
# 2[V===================]40
# 1[====GD==============]39
# G=GND (9) D=DO (11) V=VCC (1)

#SENSOR CONFIG - Set GPIO Ports
DO = 11

def setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Port d'entrada
    GPIO.setup(DO,GPIO.IN)

def main():
    setup()
    while True:
        sensor_state = GPIO.input(DO)
        if sensor_state == 0:
            print("Fum detectat")
            #dweepy.dweet_for('sensor_fum', {'Estat':'Fum detectat'})
        else:
            print("No hi ha fum")
            #dweepy.dweet_for('sensor_fum', {'Estat':'Encès'})
        print "dweeted"         
        time.sleep(1)
try:
    main()
finally:
    GPIO.cleanup()
    print("Tot tancat. Fi")
#Fi
