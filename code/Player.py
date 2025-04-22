import RPi.GPIO as gpio
from rpi_ws281x import Color
import colors

class Player():
    _gpio_initialized = False

    def __init__(self, name, button_pin, button_light_pin, light_strip):
        self._initialize_gpio()

        self.name = name
        self.button_pin = button_pin
        self.button_light_pin = button_light_pin

        gpio.setup(self.button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.button_light_pin, gpio.OUT)
        gpio.output(self.button_light_pin, gpio.HIGH)
        
        self.light_strip = light_strip
           
        self.current_state = 1
        self.active = False
        self.disabled = False

    def _initialize_gpio(self):
        if not Player._gpio_initialized:
            gpio.setmode(gpio.BCM)
            Player._gpio_initialized = True

    def change_light_strip_color(self, color):
        print(self.name, color)
        if(self.name == "P4" or self.name == "P1"):
            print('ws library players')
            print(color)
            ws_color = Color(0,0,0)
            if(color == colors.RED):
                ws_color = Color(255,0,0)
            elif(color == colors.GREEN):
                ws_color = Color(0,255,0)
            elif(color == colors.YELLOW):
                ws_color = Color(255,255,0)
            elif(color == colors.WHITE):
                ws_color = Color(255,255,255)
            
            print(ws_color)
            for i in range(self.light_strip.numPixels()):
                self.light_strip.setPixelColor(i, ws_color)
            self.light_strip.show()
        else:
            self.light_strip.fill(color)

    def button_light_on(self):
        gpio.output(self.button_light_pin, gpio.LOW)

    def button_light_off(self):
        gpio.output(self.button_light_pin, gpio.HIGH)

    def input_from_button(self):
        return gpio.input(self.button_pin)
