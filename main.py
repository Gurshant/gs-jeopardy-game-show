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
        
    def game(self): #Returns first button pressed

        #Check for button presses
        while True:
            self.winner = self.check()
            if self.winner != '':
                break
        return self.winner

    def check(self):
        print('running')
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

        return self.winner

    def is_button_clicked(self, player):
        if player.input_from_button() == 0:
#             start threads
            sounds.play_buzzer_pressed()
            t2 = threading.Thread( target=self.turn_light_on, args=(player,))
            t2.start()
#             wait for thread execution
            t2.join()
            print("after play")
            return True
        else:
            return False
        
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
