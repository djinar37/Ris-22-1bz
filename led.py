from gpiozero import LED
from time import sleep

led = LED(15)
led.on()
sleep(5)
led.off()

