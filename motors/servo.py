import RPi.GPIO as GPIO
import time

motor_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_pin,GPIO.OUT)

pwm = GPIO.PWM(motor_pin,100)
pwm.start(5)

try:
    while True:
        duty = int(input("Entrar angulo (0 a 100): "))
        pwm.ChangeDutyCycle(duty)

finally:
    print("Cleaning up")
    GPIO.cleanup()
