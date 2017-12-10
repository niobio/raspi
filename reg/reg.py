import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# El pin a carrega el condensador a través d'una resistència fixa d'1k 
# i el potenciómetre en sèrie.
# El pin b descarrega el condensador a través de la resistència d'1k

pin_a = 16
pin_b = 18
pinout = 12

GPIO.setup(pinout, GPIO.OUT)

# Funció per la descàrrega del condensador, deixant-lo buit per a començar la càrrega
def descarrega():
    GPIO.setup(pin_a, GPIO.IN)
    GPIO.setup(pin_b, GPIO.OUT)
    GPIO.output(pin_b, False)
    time.sleep(0.1)

# Funció que retorna el temps de càrrega del condensador en microsegons fins arribar
# al nivell HIGH, el qual és major o igual a 1.65V.
def temps_carrega():
    GPIO.setup(pin_b, GPIO.IN)
    GPIO.setup(pin_a, GPIO.OUT)
    GPIO.output(pin_a, True)
    t1 = time.time()
    while not GPIO.input(pin_b):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

# Funció que pren el temps de càrrega del condensador com a lectura analògica
# després de primer descarregar el condensador
def lectura_analog():
    descarrega()
    t = temps_carrega()
    descarrega()
    return t

try:
    while True:
        t = lectura_analog()
        print(t)
        if t < 70:
            GPIO.output(pinout, True)
        else:
            GPIO.output(pinout, False)
        time.sleep(5)
finally:
    GPIO.cleanup()
