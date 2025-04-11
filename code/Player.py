import RPi.GPIO as gpio
import neopixel

class Player():
    # light needs to be a board value and the rest are pins
    def __init__(self, name, button, button_light,light_strip):
        gpio.setmode(gpio.BCM)
        self.name = name
        self.button_pin = button
        self.button_light_pin = button_light
        self.current_state  = 1
        gpio.setup(self.button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.button_light_pin, gpio.OUT)
        gpio.output(self.button_light_pin, gpio.HIGH)

        self.light_strip = neopixel.NeoPixel(light_strip, 55, brightness=1)
        
        self.active = False
        self.disabled = False

    def change_light_strip_color(self, color):
        self.light_strip.fill(color)

    def button_light_on(self):
        gpio.output(self.button_light_pin, gpio.LOW)

    def button_light_off(self):
        gpio.output(self.button_light_pin, gpio.HIGH)

    def input_from_button(self):
        return gpio.input(self.button_pin)
