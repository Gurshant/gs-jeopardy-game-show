import RPi.GPIO as gpio
import time
import player
import sounds

class Game():
    def __init__(self):
        #Setup pins and board
        self.p1 = player.Player("Player 1",4,5)
        self.p2 = player.Player("Player 2",26,6)
#         self.p3 = player.Player("Player 3",21,7)
#         self.p4 = player.Player("Player 4",22,8)
        self.first = ''


    def reset(self):
        self.first = ''
        
    def game(self): #Returns first button pressed

        #Check for button presses
        while True:
            self.first = self.check()
            if self.first != '':
                break
        return self.first

    def check(self):
        print('running')
        if self.is_button_clicked(self.p1):
            self.first = '1'
        elif self.is_button_clicked(self.p2):
            self.first = '2'
#         elif self.is_button_clicked(self.p3):
#             self.first = '3'
#         elif self.is_button_clicked(self.p4):
#             self.first = '4'
        else:
            pass

        return self.first

    def is_button_clicked(self, player):
        if player.input_from_button() == 0:
            self.sounds.playRightAnswer()
            self.turn_light_on(player)

            return True
        else:
            return False
        
    def turn_light_on(self, player):
        player.light_on()
        time.sleep(5.5)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(1)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(1)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(1)
        player.light_off()
    
if __name__ == '__main__':
    test = Game()
    while True:
        test.first = ''
        winner = test.game()
        print (winner)
    gpio.cleanup()
