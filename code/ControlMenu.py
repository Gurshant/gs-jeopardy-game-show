import pygame
import sys
import Game
import Sounds
import colors
import button
import RPi.GPIO as gpio

class ControlMenu:
    WIDTH = 750
    HEIGHT = 500
    BIG_WIDTH = 300
    BIG_HEIGHT = 70
    SMALL_WIDTH = 40
    SMALL_HEIGHT = 150
    BIG_FONT_SIZE = 45
    SMALL_FONT_SIZE = 25

    def __init__(self, steal_mode=False):
        gpio.setwarnings(False)
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game Control Menu")

        self.font_big = pygame.font.SysFont('arial', 40)
        self.font_small = pygame.font.SysFont('arial', 25)

        self.game = Game.Game(steal_mode=steal_mode)
        self.buttons = []
        self.setup_buttons()

    def setup_buttons(self):
        row1_y = 120
        row2_y = self.HEIGHT / 2 + 100
        row3_y = self.HEIGHT - 50

        self.buttons = [
            button.button(colors.GREEN, self.BIG_FONT_SIZE, 50, row1_y, self.BIG_WIDTH, self.BIG_HEIGHT, 'Correct (y)', self.game.correct_ans),
            button.button(colors.RED, self.BIG_FONT_SIZE, self.WIDTH / 2 + 25, row1_y, self.BIG_WIDTH, self.BIG_HEIGHT, 'Incorrect (n)', self.game.incorrect_ans),
            button.button(colors.BLUE, self.SMALL_FONT_SIZE, 50, row2_y, self.SMALL_HEIGHT, self.SMALL_WIDTH, 'Reset (r)', self.game.reset),
            button.button(colors.YELLOW_GREEN, self.SMALL_FONT_SIZE, self.WIDTH / 3 + 125, row2_y, self.SMALL_HEIGHT, self.SMALL_WIDTH, 'Yes Sound', Sounds.correct),
            button.button(colors.YELLOW_RED, self.SMALL_FONT_SIZE, self.WIDTH * 2 / 3 + 50, row2_y, self.SMALL_HEIGHT, self.SMALL_WIDTH, 'No Sound', Sounds.incorrect),
            button.button(colors.RED, self.SMALL_FONT_SIZE, self.WIDTH * 2 / 3 + 50, row3_y, self.SMALL_HEIGHT, self.SMALL_WIDTH, 'Quit (q)', self.quit_game)
        ]

    def draw_screen(self):
        self.screen.fill((0, 0, 0)) 
        self.screen.blit(self.font_big.render("Controls", True, (255, 255, 255)), (self.WIDTH / 2 - 70, 50))
        self.screen.blit(self.font_big.render("ADMIN USE ONLY**", True, (255, 255, 255)), (self.WIDTH / 2 - 200, self.HEIGHT / 2))
        for b in self.buttons:
            b.draw(self.screen)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            elif event.type == pygame.KEYDOWN:
                keymap = {
                    'q': self.quit_game,
                    'y': self.game.correct_ans,
                    'n': self.game.incorrect_ans,
                    'r': self.game.reset
                }
                keyname = pygame.key.name(event.key)
                if keyname in keymap:
                    keymap[keyname]()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for b in self.buttons:
                    if b.isOver(pygame.mouse.get_pos()):
                        b.callback()

    def quit_game(self):
        pygame.quit()
        gpio.cleanup()
        sys.exit()

    def run_game(self):
        while not self.game.check():
            self.draw_screen()
            self.handle_events()

if __name__ == '__main__':
    ControlMenu().run_game()