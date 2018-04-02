import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

try:
    while True:
        input_state = GPIO.input(12)
        if input_state == True:
            print('Moviment detectat')
            time.sleep(1)
except KeyboardInterrupt:
    print("Ctrl + C, Quit")
finally:
    GPIO.cleanup()
    
