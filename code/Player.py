import RPi.GPIO as gpio

class Player():
    def __init__(self, name, button, light):
        gpio.setmode(gpio.BCM)
        self.name = name
        self.button_pin = button
        self.light_pin = light
        self.current_state  = 1
        gpio.setup(self.button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

        gpio.setup(self.light_pin, gpio.OUT)
        gpio.output(self.light_pin, gpio.HIGH)
        
        self.active = False
        self.disabled = False

    def light_on(self):
        gpio.output(self.light_pin, gpio.LOW)
    
    def light_off(self):
        gpio.output(self.light_pin, gpio.HIGH)
        
    def input_from_button(self):
        return gpio.input(self.button_pin)
        