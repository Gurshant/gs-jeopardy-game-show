import pygame
import sys
import Game
import Sounds
import colors
import button
import RPi.GPIO as gpio

class ControlMenu():
    
    def __init__(self, steal_mode = False):
        gpio.setwarnings(False)
        pygame.init()
        self.width = 750
        self.height = 500
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.game = Game.Game(steal_mode)
        
        text = pygame.font.SysFont('arial', 40).render("Controls", 1, (255,255,255))
        self.screen.blit(text, (self.width/2-70,50))
        
        text = pygame.font.SysFont('arial', 40).render("ADMIN USE ONLY**", 1, (255,255,255))
        self.screen.blit(text, (self.width/2-200,self.height/2))
        
        
        
        self.__init__buttons__()
    
    def __init__buttons__(self):
        row1_height = 120
        row2_height = self.height/2+100
        row3_height = self.height-50
        big_width = 300
        big_height =70
        big_font_size = 45
        small_width = 40
        small_height = 150
        small_font_size = 25
        self.buttons = [
            button.button(colors.GREEN,big_font_size,50,row1_height,big_width,big_height,'Correct (y)', self.correct_ans),
            button.button(colors.RED,big_font_size, self.width/2+25,row1_height,big_width,big_height,'Incorrect (n)', self.incorrect_ans),
            
            button.button(colors.BLUE,small_font_size,50,row2_height,small_height,small_width,'Reset (r)', self.game.reset),
            button.button(colors.YELLOW_GREEN,small_font_size, self.width/3+125,row2_height,small_height,small_width,'Yes Sound', Sounds.correct),
            button.button(colors.YELLOW_RED,small_font_size, self.width*2/3+50,row2_height,small_height,small_width,'No Sound', Sounds.incorrect),
            
            button.button(colors.RED,small_font_size, self.width*2/3+50,row3_height,small_height,small_width,'Quit (q)', self.quit_game)
        ]
        for b in self.buttons:
            b.draw(self.screen)

    def event_handler(self):
        for ev in pygame.event.get():
            # if quitting
            if ev.type == pygame.QUIT:
                self.quit_game()
                
            if ev.type == pygame.KEYDOWN:
                if pygame.key.name(ev.key) == 'q':
                    self.quit_game()
                elif pygame.key.name(ev.key) == 'y':
                    self.correct_ans()
                elif pygame.key.name(ev.key) == 'n':
                    self.incorrect_ans()
                elif pygame.key.name(ev.key) == 'r':
                    self.game.reset()
                # fail safe for just sounds
#                 elif pygame.key.name(ev.key) == 'c':
#                     Sounds.correct()
#                 elif pygame.key.name(ev.key) == 'w':
#                     Sounds.incorrect()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                for b in self.buttons:
                    if b.isOver(pygame.mouse.get_pos()):
                        b.callback()
                    
            # updates the frames of the game
            pygame.display.update()
    def quit_game(self):
        pygame.quit()
        sys.exit()
        
    def correct_ans(self):
        Sounds.correct()
        self.game.reset()
    
    def incorrect_ans(self):
        Sounds.incorrect()
        if self.game.steal_mode:
            self.game.disable_player()
        else:
            self.game.reset()
        
        
    def run_game(self):
        winner = ''
        while winner == '':
            self.game.check() 
            self.event_handler()
        
        gpio.cleanup()

if __name__ == '__main__':
#   For round 1 
    steal_mode = True
#   For round 2
#     steal_mode = False
    menu = ControlMenu(steal_mode)
    menu.run_game()
