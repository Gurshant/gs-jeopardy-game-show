import RPi.GPIO as gpio
import time

class Poll():
    def __init__(self):
        self.DEBUG = True

        #Setup pins and board
        gpio.setmode(gpio.BCM)
        # Input high by default
        gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP)
 
        gpio.setup(5, gpio.OUT)
        gpio.output(5, gpio.HIGH)

        #Put pins in variables
        self.center_button = 4
        
        self.first = ''

        self.center_press = 1

    def reset(self):
        self.first = ''

        self.center_press = 1
        
    def poll(self): #Returns first button pressed
        #Variables for press count (one for each button)
        self.center_press = 1
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
        center_input = gpio.input(self.center_button)
        print('center_input')

        print(center_input)

        if center_input == 0:
            print('ADMIN: Console button 2 has been pressed')
#            
            gpio.output(5, gpio.LOW)
            time.sleep(1.5)
            gpio.output(5, gpio.HIGH)
            time.sleep(1)

            gpio.output(5, gpio.LOW)
            time.sleep(1.5)
            gpio.output(5, gpio.HIGH)
            self.first = 1
        else:
            pass


#         if center_input == True:
#         print('center_press')

#         print(self.center_press)
#         if self.center_press == 0:
#             print('ADMIN: Console button 2 has been pressed')
                
#                 self.first = 1
#             gpio.output(5, gpio.LOW)
#             time.sleep(1)
#             gpio.output(5, gpio.HIGH)

#         else:
#             pass
#             print('ADMIN: Console button 2 has been pressed')

#         self.center_press += 1

        return self.first

if __name__ == '__main__':
    test = Poll()
    test.poll()
    gpio.cleanup()
#     while True:
#         test.first = ''
#         winner = test.poll()
#     print (winner)