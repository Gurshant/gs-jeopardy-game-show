import time
import threading
import Player
import Sounds
import board
import colors

class Game():
    def __init__(self, steal_mode = False):
        self.winners = ''
        #Setup pins and board
        self.players = [
            #Player.Player("Player 1",3,5,board.D10),
            Player.Player("Player 1", 15, 23, board.D12),
            #Player.Player("Player 2", 6, 9, board.D12),
            #Player.Player("Player 3", 24, 7, board.D10),
            #Player.Player("Player 4", 12, 8, board.D21)
        ]
        self.abort_thread = False
        self.steal_mode = True
        

    def reset(self):
        self.abort_thread = True
        time.sleep(1.5)
        print('Reset Game')
        self.winner = ''
        self.reset_players()
        

    def disable_player(self):
        count = 0
        self.abort_thread = True
        for p in self.players:
            if p.active:
                print('Disabled ' + p.name)
                p.disabled = True
                count += 1
        if count > 1:
            self.reset()
    
    def check(self):
        for p in self.players:
            if self.is_button_clicked(p):
                self.winners = p.name
        return self.winners

    def is_button_clicked(self, player):
        prior = player.current_state
        player.current_state = player.input_from_button()
        
        if player.current_state == 0 and prior == 1 and not player.disabled:
            for th in threading.enumerate():
                if th.name == 'light':
                    print(player.name)
                    return False
            self.abort_thread = False
            threading.Thread( target=self.button_clicked, args=(player, ), name='light').start()
            print(player.name)
            print('create thread')
            return True
        else:
            return False

    def button_clicked(self, player):
        player.active = True
        Sounds.incorrect()
        player.button_light_on()
        self.turn_light_on(player, 10)

    def turn_light_on(self, player, seconds):
        s_elapsed = 0
        while s_elapsed < seconds:
            if self.abort_thread:
                print('abort')
                self.abort_thread = False
                player.change_light_strip_color(colors.BLACK)
                s_elapsed = seconds
                return
            elif seconds - s_elapsed < 5:
                player.change_light_strip_color(colors.WHITE)
                time.sleep(.25)
                player.change_light_strip_color(colors.BLACK)
                time.sleep(.25)
            else:
                player.change_light_strip_color(colors.WHITE)
                time.sleep(.5)
            s_elapsed += .5
        self.incorrect_ans()

    def reset_players(self):
        print('reset_players')
        for p in self.players:
            p.disabled = False
            p.active = False
            p.button_light_off()
            p.change_light_strip_color(colors.WHITE)

    def incorrect_ans(self):
        for p in self.players:
            if p.active:
                p.change_light_strip_color(colors.RED)
        Sounds.incorrect()
        
        if self.steal_mode:
            self.disable_player()
        else:
            self.reset()

    def correct_ans(self):
        for p in self.players:
            if p.active:
                p.change_light_strip_color(colors.GREEN)
        Sounds.correct()
        self.reset()

    def round_1(self):
        print('Round 1 (Steal Mode)')
        self.steal_mode = True

    def round_2(self):
        print('Round 2 (Speed )')
        self.steal_mode = False
