from gpiozero import Button

button = Button(6)

button.wait_for_press()
print('You pushed me')
