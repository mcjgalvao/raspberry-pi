from gpiozero import LED
from time import sleep
from gpiozero import Button

led = LED(18)
button = Button(6)

while True:
    button.wait_for_press()
    led.on()
    sleep(0.3)
    button.wait_for_press()
    led.off()
    sleep(0.3)

