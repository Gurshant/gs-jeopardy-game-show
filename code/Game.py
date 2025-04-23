import time
import threading
import Player
import Sounds
import board
import colors
import neopixel
from rpi_ws281x import PixelStrip, ws

class Game():
    def __init__(self):
        self.winners = ''
        #Setup pins and board
        strip_a = PixelStrip(30, 18, 1000000, 10, False, 255, 0, ws.WS2811_STRIP_GRB)
        #strip_a = neopixel.NeoPixel(board.D18, 30, brightness=1)
        strip_b = neopixel.NeoPixel(board.D21, 30, brightness=1)
        strip_c = neopixel.NeoPixel(board.D10, 30, brightness=1)
        strip_d = PixelStrip(30, 13, 800000, 10, False, 255, 1, ws.WS2811_STRIP_GRB)
        strip_d.begin()
        strip_a.begin()
        
        self.players = [
            Player.Player("P1", 15, 23, strip_a),
            Player.Player("P2", 11, 9, strip_b),
            Player.Player("P3", 25, 20, strip_c),
            Player.Player("P4", 17, 26, strip_d)
        ]
        self.abort_thread = False
        self.steal_mode = True
        self.reset()

    def reset(self):
        self.abort_thread = True
        print('Reset Game')
        self.winners = ''
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
            time.sleep(1.5)
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
            threading.Thread( target=self.button_clicked, args=(player, ), name='light', daemon=True).start()
            print(player.name)
            print('create thread')
            return True
        return False

    def button_clicked(self, player):
        print('button_clicked', player.name)
        player.active = True
        Sounds.buzzer()
        player.button_light_on()
        self.turn_light_on(player, 10)

    def turn_light_on(self, player, seconds):
        s_elapsed = 0
        while s_elapsed < seconds and not self.abort_thread:
            if seconds - s_elapsed < 5:
                print("SET TO WHITE")
                player.change_light_strip_color(colors.WHITE)
                time.sleep(.25)
                if not self.abort_thread:
                    player.change_light_strip_color(colors.BLACK)
                    time.sleep(.25)
                if seconds - s_elapsed <= .5:
                    self.incorrect_ans()
            else:
                print("SET TO WHITE")
                player.change_light_strip_color(colors.WHITE)
                time.sleep(.5)
            s_elapsed += .5
        
        if self.abort_thread:
            print('thread aborted')
            self.abort_thread = False
            return

    def reset_players(self):
        print('reset_players')
        for p in self.players:
            p.disabled = False
            p.active = False
            p.button_light_off()
            p.change_light_strip_color(colors.BLACK)
            
    def waiting_state(self):
        print('waiting state')
        for p in self.players:
            p.disabled = True
            p.active = False
            p.button_light_off()
            p.change_light_strip_color(colors.YELLOW)

    def incorrect_ans(self):
        print('incorrect')
        self.abort_thread = True
        Sounds.incorrect()
        for p in self.players:
            print(p.name, p.active)
            if p.active:
                p.change_light_strip_color(colors.RED)
        
        if self.steal_mode:
            self.disable_player()
        else:
            time.sleep(1.5)
            self.reset()

    def correct_ans(self):
        self.abort_thread = True
        Sounds.correct()
        for p in self.players:
            print(p.name, p.active, p.disabled)
            if p.active and not p.disabled:
                p.change_light_strip_color(colors.GREEN)
        time.sleep(1.5)
        self.reset()
