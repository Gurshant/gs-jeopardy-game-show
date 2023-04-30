import RPi.GPIO as gpio
import time
import player

class Game():
    def __init__(self):
        #Setup pins and board
        gpio.setmode(gpio.BCM)

        p1 = player.Player(4,5)
        p2 = player.Player(20,6)
        p3 = player.Player(21,7)
        p4 = player.Player(22,8)

        # gpio.setup(pins.P1_BUTTON, gpio.IN, pull_up_down=gpio.PUD_UP)
 
        # gpio.setup(pins.P1_LIGHT, gpio.OUT)
        # gpio.output(pins.P1_LIGHT, gpio.HIGH)

        #Put pins in variables
        # self.center_button = pins.P1_BUTTON
        
        self.first = ''


    def reset(self):
        self.first = ''
        
    def game(self): #Returns first button pressed
        #Variables for press count (one for each button)
#         self.right_press = 0
#         self.left_press = 0

        #Check for button presses
        while True:
            self.first = self.check()
            if self.first != '':
                break
        time.sleep(.5)
        return self.first

    def check(self):
        center_input = gpio.input(self.p1.button_pin)
        print('center_input')

        print(center_input)

        if center_input == 0:
            print('ADMIN: Console button 2 has been pressed')
#            
            gpio.output(5, gpio.LOW)
            self.p1.light_on
            time.sleep(1.5)
            self.p1.light_off
            # gpio.output(5, gpio.HIGH)
            time.sleep(1)
            self.p1.light_on

            # gpio.output(5, gpio.LOW)
            time.sleep(1.5)
            self.p1.light_off

            # gpio.output(5, gpio.HIGH)
            self.first = 1
        else:
            pass


#         if center_input == True:

#             print('ADMIN: Console button 2 has been pressed')
                
#                 self.first = 1
#             gpio.output(5, gpio.LOW)
#             time.sleep(1)
#             gpio.output(5, gpio.HIGH)

#         else:
#             pass
#             print('ADMIN: Console button 2 has been pressed')


        return self.first

if __name__ == '__main__':
    test = Game()
    test.poll()
    gpio.cleanup()
#     while True:
#         test.first = ''
#         winner = test.poll()
#     print (winner)