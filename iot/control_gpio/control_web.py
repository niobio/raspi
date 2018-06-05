from bottle import route, run
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led_pins = [12, 16]
led_states = [0, 0]
switch_pin = 18

GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_status():
    state = GPIO.input(switch_pin)
    if state:
        return "ON"
    else:
        return "OFF"

def html_for_led(led):
    l = str(led)
    result = "<input type='button' onClick='changed'()" + l + ")' value='LED " + l + "'/>"
    return result

def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)
    
@route('/')
@route('/<led>')
def index(led):
    if led >= '0' and led <='1':
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "    window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>GPIO Control</h1>'
    response += '<h2>Button=' + switch_status() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += html_for_led(0)
    response += html_for_led(1)
    return response

try:
    run(host='0.0.0.0', port=8080)
finally:
    print('\nCleaning up')
    GPIO.cleanup()

