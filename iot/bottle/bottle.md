
# Servidor web senzill amb Python

Una manera senzilla de publicar a internet l'estat de sensors i, fins i tot, controlar sensors i actuadors de manera remota és mitjançant un servidor web al poder connectar. Veurem ara com fer funcionar la nostra Raspberry Pi com un servidor web senzill per fer coses com aquestes. No necessitem instal·lar un servidor potent (tampoc en volem) per fer coses senzilles. Per això utilitzarem la biblioteca `bottle` que ens permetrà tenir un servidor web senzill a la nostra placa. 

Per a instal·lar `bottle` a la Raspberry utilitzarem l'ordre:

`sudo apt install python-bottle`

al terminal d'ordres. Per a que pugui descarregar el paquet hem de tenir connexió a internet.

Un cop instal·lada la biblioteca podem provar-la fent córrer el següent script que el que fa es publicar a la web la data i hora actual:


```python
from bottle import route, run, template
from datetime import datetime

@route('/')
def index(name='time'):
    dt = datetime.now()
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template('<b>Pi thinks the date/time is: {{t}}</b>', t=time)

run(host='0.0.0.0', port=8080)
```

Després d'importar les biblioteques, l'ordre `@route` enllaça l'adreça d'ubicació `/` amb la funció que es troba a continuació. La funció el que fa és crear una cadena amb la data i hora actuals en format HTML i la retorna al servidor per a ser visualitzada. En aquest cas utilitza una plantilla (`template`) en el qual els valors són substituits.

La línia final arrenca els procés de servir la pàgina al servidor. Si podem coma valor de `host` l'adreça `'0.0.0.0'` aquesta serà reemplaçada per l'adreça web de la Raspberry Pi. El port 8080 és el port on es podrà anar a buscar la pàgina i, de ser necessari aquest número es pot canviar.
