import RPi.GPIO as GPIO
 
ObstaclePin = 11
 
def setup():
    GPIO.setmode(GPIO.BOARD) # Set GPIO by numbers 
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
def loop():
    while True:
        if (0 == GPIO.input(ObstaclePin)): 
            print("14CORE | Obstacle Avoidance Sensor Test \n")
            print(" DETECTED: There is an obstacle ahead")
 
def destroy():
    GPIO.cleanup() # Release resource
 
if __name__ == '__main__': # The Program start here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Control C is pressed, the child program destroy will be executed.
        destroy()
