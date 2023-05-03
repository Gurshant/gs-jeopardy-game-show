import pygame
import sys
import Game
import Sounds
import colors
import button
import RPi.GPIO as gpio

class ControlMenu():
    
    def __init__(self):
        gpio.setwarnings(False)
        pygame.init()
        self.width = 750
        self.height = 500
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.game = Game.Game()
        self.__init__buttons__()
    
    def __init__buttons__(self):
        self.buttons = [
            button.button(colors.GREEN,60,50,50,300,70,'correct (y)', self.correct_ans),
            button.button(colors.RED,60, self.width/2+25,50,300,70,'incorrect (n)', self.incorrect_ans),
            
            button.button(colors.BLUE,25,50,self.height/2,150,40,'Reset (r)', self.game.reset),
            button.button(colors.YELLOW_GREEN,25, self.width/3+75,self.height/2,150,40,'Yes Sound', Sounds.correct),
            button.button(colors.YELLOW_RED,25, self.width*2/3+25,self.height/2,150,40,'No Sound', Sounds.incorrect),
            
            button.button(colors.RED,25, self.width*2/3,self.height-50,150,40,'Quit (q)', self.quit_game)
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
        self.game.reset()
        
        
    def run_game2(self):
        winner = ''
        while winner == '':
            self.game.check() 
            self.event_handler()
        
        gpio.cleanup()

if __name__ == '__main__':
    menu = ControlMenu()
    menu.run_game2()
