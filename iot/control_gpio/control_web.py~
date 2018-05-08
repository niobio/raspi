from bottle import route, run
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led_pins = [12, 16, 18]
led_states = [0, 0, 0]

switch_pin = 22

GPIO.setup(led.pins[0], GPIO.OUT)
GPIO.setup(led.pins[1], GPIO.OUT)
GPIO.setup(led.pins[2], GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
