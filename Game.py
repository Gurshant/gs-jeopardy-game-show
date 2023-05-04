import time
import threading
import Player
import Sounds

class Game():
    def __init__(self):
        self.winners = ''
        #Setup pins and board
        self.players = [
            Player.Player("Player 1",3,5),
            Player.Player("Player 2",23,6),
            Player.Player("Player 3",24,13),
            Player.Player("Player 4",26,19)
        ]
        self.abort_thread = False
        self.disabled_player = ''

    def reset(self):
        self.winner = ''
        self.abort_thread = True
        self.turn_all_lights_off()

    def check(self):
#         if button already enables
# TODO turn this into a loop
        if self.is_button_clicked(self.players[0]):
            self.winner = '1'
        elif self.is_button_clicked(self.players[1]):
            self.winner = '2'
        elif self.is_button_clicked(self.players[2]):
            self.winner = '3'
        elif self.is_button_clicked(self.players[3]):
            self.winner = '4'
        else:
            pass
        return self.winners

    def is_button_clicked(self, player):
        
        prior = player.current_state
        player.current_state = player.input_from_button()
        
        if player.current_state == 0 and prior == 1:
            for th in threading.enumerate():
                if th.name == 'button':
                    print('th running')
                    return False
            
            threading.Thread( target=self.button_clicked, args=(player, ), name='button').start()
            print('create thread')
            return True
        else:
            return False
    
    def button_clicked(self, player):
        Sounds.buzzer()
        self.turn_light_on(player, 10)

    def turn_light_on(self, player, seconds):
        s_elapsed = 0
        while s_elapsed < seconds:
            if self.abort_thread:
                player.light_off()
                s_elapsed = seconds
                self.abort_thread = False
                return
            elif seconds - s_elapsed < 5:
                player.light_on()
                time.sleep(.5)
                player.light_off()
                time.sleep(.5)
            else:
                player.light_on()
                time.sleep(1)
            s_elapsed += 1
        Sounds.incorrect()
    
    def turn_all_lights_off(self):
        for p in self.players:
            p.light_off()
    
    