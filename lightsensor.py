from gpiozero import LightSensor, LED

ldr, led = LightSensor(17), LED(18)

while True:
    print("Value: {0:.2f}".format(ldr.value))
    if ldr.value < 0.6:
        led.on()
    else:
        led.off()
        

    

