from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)  # broche 2 en sortie
tilt_switch = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)

while True:
    sleep_ms(100)
    if tilt_switch.value() == 1:
        led.value(1)   # allume la LED
    else:
        led.value(0)   # éteint la LED  
