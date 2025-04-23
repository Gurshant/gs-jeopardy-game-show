import pygame

class button:
    def __init__(self, color, font_size, x, y, width, height, text, callback):
        self.color = color
        self.font_size = font_size
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.font = pygame.font.SysFont('arial', font_size)

    def draw(self, surface, outline = None):
        if outline:
            pygame.draw.rect(surface, outline, self.rect.inflate(4, 4))

        pygame.draw.rect(surface, self.color, self.rect)

        if self.text:
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def isOver(self, pos):
        return self.rect.collidepoint(pos)
