
# Taller projecte Domus

## La placa de proves

La placa de proves o de prototipatge ràpid (també coneguda com *breadboard* o *protoboard* en anglès) ens permet crear circuits electrònics de manera ràpida sense necessitat de soldar els elements del circuit.

<img src="img/protoboard.jpg" style="centered" width="40%">

## La placa Raspberry Pi

<img src="img/RPi_2b.png" style="centered" width="70%">

## Els pins GPIO

<img src="img/gpio_board.jpeg" style="centered" width="50%">


## Encendre un LED

<img src="img/led_blink_esquema_bb.png" style="centered" width="40%">



```python
from gpiozero import LED
from time import sleep

led = LED(24)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

# Detecció de moviments amb infrarroigs


El sensor que es veu a la imatge inferior és un HC-SR501, es tracta d'un sensor infrarroig passiu (PIR), i serveix per a detectar moviments. Resulta habitual trobarlos als lavabos públics per encendre la llum quan detecta la presencia de persones.

<img src="img/PIR_1.jpeg" style="centered" width="40%">

<img src="img/PIR_2.jpg" style="centered" width="70%">


Si vols saber més de com funcionen els PIR pots consultar <a href="https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work" target="_blank">aquesta pàgina</a>.

A continuació tenim un exemple de codi que permet detectar el moviment:


```python
from gpiozero import MotionSensor, LED
from time import sleep

led = LED(24)
pir = MotionSensor(22)

while True:
    pir.wait_for_motion()
    print("Moviment detectat!")
    led.on()
    sleep(2)
    led.off()
```
