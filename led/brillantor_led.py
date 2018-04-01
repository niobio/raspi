import RPi.GPIO as GPIO

led_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

pwd_led = GPIO.PWM(led_pin, 500)
pwd_led.start(100)

while True:
    duty = int(input("Introdueix la brillantor (0 a 100): "))
    pwm_led.ChangeDutyCycle(duty)
