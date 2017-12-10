
# Sensors digitals amb Raspberry Pi

Els sensors digitals son dispositius que admeten dos possibles estats com ser encès/apagat, sí/no, veritat/fals, etc.

El cas més típic és el d'un polsador o un interruptor que admet l'estat connectat o desconnectat. 

Veurem ara com gestionar amb la Raspberry Pi la informació donada per un sensor digital com un polsador. Conectarem el polsador a un pin de la Raspberry i per fer-ho provarem dues possibilitats, connectar-lo fent servir una resistència *pull up* o fent servir una resistència *pull down*. La forma de connexió es pot veure a la figura següent:

<img src="img/pull-up_pull-down.png" width=400>

En la connexió *pull down* el pin de la Raspberry, quan el polsador està en repòs, té un voltatge null. El polsador té un terminal connectat a la font d'alimentació i l'altre connectat a la resistència que està connactada a terra (GND). Vout indica el punt de connexió al pin d'entrada de la Raspberry, si el polsador està obert Vout té un voltatge de 0 volts (estat 0) i quan el polsador està polsat, el voltatge Vout té el valor 5V (estat 1).

En la connexió *pull up* el pin de la Raspberry té un voltatge Vcc = 5V quan està el polsador està en repòs i passa a zero quan es prem el botó. Un valor típic de la resistència és d'$1\,\mathrm{k\Omega}$.

## Codi en Python

Crearem un programa per a gestionar la informació donada pel sensor digital. Utilitzarem un polsador en connexió pull down i farem que el programa imprimeixi en la pantalla del terminal l'estat del polsador. 


```python
import RPi.GPIO as GPIO
import time

pols = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pols, GPIO.IN)    # pin 9 utilitzat com entrada del sensor

# bucle infinit
while 1:
    if GPIO.input(pols) == 1:
        print("Polsador premut")
    elif GPIO.input(pols) == 0:
        print("Polsador lliure")
    time.sleep(0.5)
```

El programa està sempre comprovant cada mig segon si el polsador ha estat premut i informa del seu estat. En aquest exemple hem fet que s'imprimeixi en la pantalla l'estat del polsador però també es pot fer que s'accionés un actuador, com ser encendre un motor o un altre dispositiu, depenent de l'estat del sensor, la qual cosa és l'ús més habitual dels sensors.
