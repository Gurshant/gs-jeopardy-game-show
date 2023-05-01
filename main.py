import RPi.GPIO as gpio
import time, threading
import player, sounds

class Game():
    def __init__(self):
        #Setup pins and board
        self.p1 = player.Player("Player 1",4,5)
        self.p2 = player.Player("Player 2",26,6)
#         self.p3 = player.Player("Player 3",21,7)
#         self.p4 = player.Player("Player 4",22,8)
        self.winner = ''


    def reset(self):
        self.winner = ''

    def check(self):
#         if button already enables
        if self.is_button_clicked(self.p1):
            self.winner = '1'
        elif self.is_button_clicked(self.p2):
            self.winner = '2'
#         elif self.is_button_clicked(self.p3):
#             self.winner = '3'
#         elif self.is_button_clicked(self.p4):
#             self.winner = '4'
        else:
            pass
        
        print('still?')

        return self.winner

    def is_button_clicked(self, player):
        if player.input_from_button() == 0:
#             start threads
            for th in threading.enumerate():
                print(th.name)
                if th.name == 'button':
                    print("Thread still running")
                    return False
            
            self.button_thread = threading.Thread( target=self.button_clicked, args=(player, ), name='button').start()
#             wait for thread execution
            
            return True
        else:
            return False
    def button_clicked(self, player):
        sounds.buzzer()
        self.turn_light_on(player)

    def turn_light_on(self, player):
        player.light_on()
        time.sleep(3)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(.5)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(.5)
        player.light_off()
        time.sleep(.5)
        player.light_on()
        time.sleep(.5)
        player.light_off()

if __name__ == '__main__':
    test = Game()
    while True:
        test.winner = ''
        winner = test.game()
        print (winner)
    gpio.cleanup()
