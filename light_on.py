from gpiozero import LED, Button
from guizero import App, PushButton, Text
from signal import pause

led = LED(17)
button = Button(2)

app = App(title = "Light Bulb!")
def light_on():
    button.when_pressed = led.on
    button.when_released = led.off

on_light = PushButton(app, command = light_on, text = "On/Off")

app.display()
