import time
import multiprocessing
import Player
import Sounds

class Game():
    def __init__(self):
        self.winners = ''
        #Setup pins and board
        self.players = [
            Player.Player("Player 1",3,5),
            Player.Player("Player 2",26,6)
            # player.Player("Player 3",21,7),
            # player.Player("Player 4",22,8)
        ]
        self.button_process = None

    def reset(self):
        self.winner = ''
        self.kill_process()
        self.turn_all_lights_off()

    def check(self):
#         if button already enables
        if self.is_button_clicked(self.players[0]):
            self.winner = '1'
        elif self.is_button_clicked(self.players[1]):
            self.winner = '2'
#         elif self.is_button_clicked(self.p3):
#             self.winner = '3'
#         elif self.is_button_clicked(self.p4):
#             self.winner = '4'
        else:
            pass
        return self.winners

    def is_button_clicked(self, player):
        
        prior = player.current_state
        player.current_state = player.input_from_button()
        
        if player.current_state == 0 and prior == 1:
            
# TODO could maybe cleanup to a .find
            if self.button_process.is_alive():
                return False
            
            self.button_process = multiprocessing.Process( target=self.button_clicked, args=(player, ), name='button').start()
            return True
        else:
            return False
    
    def button_clicked(self, player):
        Sounds.buzzer()
        self.turn_light_on(player)

    def turn_light_on(self, player):
#         TODO improve this
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
        Sounds.buzzer()
        player.light_off()
    
    def turn_all_lights_off(self):
        for p in self.players:
            p.light_off()
    
    def kill_process(self):
        self.button_process.terminate()