import RPi.GPIO as gpio
import neopixel

class Player():
    _gpio_initialized = False

    def __init__(self, name, button_pin, button_light_pin, light_strip_board):
        self._initialize_gpio()

        self.name = name
        self.button_pin = button_pin
        self.button_light_pin = button_light_pin
        
        gpio.setup(self.button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.button_light_pin, gpio.OUT)
        gpio.output(self.button_light_pin, gpio.HIGH)

        self.light_strip = neopixel.NeoPixel(light_strip_board, 55, brightness=1)

        self.current_state = 1
        self.active = False
        self.disabled = False

    def _initialize_gpio(self):
        if not Player._gpio_initialized:
            gpio.setmode(gpio.BCM)
            Player._gpio_initialized = True

    def change_light_strip_color(self, color):
        print('color', color)
        self.light_strip.fill(color)

    def button_light_on(self):
        gpio.output(self.button_light_pin, gpio.LOW)

    def button_light_off(self):
        gpio.output(self.button_light_pin, gpio.HIGH)

    def input_from_button(self):
        return gpio.input(self.button_pin)
