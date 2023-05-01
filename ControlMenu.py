import pygame
import sys
import Game
import Sounds
import threading
import RPi.GPIO as gpio

class ControlMenu():
    
    def __init__(self):
        gpio.setwarnings(False)
        # initializing the constructor
        pygame.init()
        # opens up a window
        self.screen = pygame.display.set_mode((720,720))
        # white color
        self.color = (255,255,255)
        # light shade of the button
        self.color_light = (170,170,170)
        # dark shade of the button
        self.color_dark = (100,100,100)
        # stores the width of the screen into a variable
        self.width = self.screen.get_width()
        # stores the height of the screen into a variable
        self.height = self.screen.get_height()
        # rendering a text written in this font
        self.text = pygame.font.SysFont('Corbel',35).render('quit' , True , self.color)
        # superimposing the text onto our button
        self.screen.blit(self.text , (self.width/2+50,self.height/2))
        
        self.game = Game.Game()

    def handle_event(self):
        for ev in pygame.event.get():
            # if quitting
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if pygame.key.name(ev.key) == 'q':
                    pygame.quit()
                    sys.exit()
                # if correct answer
                elif pygame.key.name(ev.key) == 'y':
                    Sounds.correct()
                    self.game.reset()
                # if incorrect
                elif pygame.key.name(ev.key) == 'n':
                    Sounds.incorrect()
                    self.game.reset()
                # fail safe for just sounds
                elif pygame.key.name(ev.key) == 'c':
                    Sounds.correct()
                elif pygame.key.name(ev.key) == 'w':
                    Sounds.incorrect()

            # stores the (x,y) coordinates into the variable as a tuple
            mouse = pygame.mouse.get_pos()
            
            #if mouse
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the button the game is terminated
                if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <= mouse[1] <= self.height/2+40:
                    pygame.quit()
                    sys.exit()
                    
            # if mouse is hovered on a button it changes to lighter shade
            if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <= mouse[1] <= self.height/2+40:
                pygame.draw.rect(self.screen,self.color_light,[self.width/2,self.height/2,140,40])
            else:
                pygame.draw.rect(self.screen,self.color_dark,[self.width/2,self.height/2,140,40])
            
            # updates the frames of the game
            pygame.display.update()

    def run_game2(self):
        winner = ''
        while winner == '':
            print ('run')
            self.game.check() 
            self.handle_event()
            
        
        gpio.cleanup()

if __name__ == '__main__':
    menu = ControlMenu()
    menu.run_game2()
