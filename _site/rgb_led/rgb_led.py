import RPi.GPIO as GPIO

pins = {'pin_R':10, 'pin_G':11, 'pin_B':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 500)  # set Frequece to 500Hz
p_G = GPIO.PWM(pins['pin_G'], 500)
p_B = GPIO.PWM(pins['pin_B'], 500)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)
p_B.start(0)

try:
	while True:
        duty_R = float(input("Enter red component (0 to 100): "))
        duty_G = float(input("Enter green component (0 to 100): "))
        duty_B = float(input("Enter blue component (0 to 100): "))
        p_R.ChangeDutyCycle(duty_R)
        p_G.ChangeDutyCycle(duty_G)
        p_B.ChangeDutyCycle(duty_B)

except KeyboardInterrupt:
    print("Ctrl + C, quit")
	p_R.stop()
	p_G.stop()
	p_B.stop()
finally:
	GPIO.cleanup()

