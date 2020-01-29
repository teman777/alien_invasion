import pygame

class GameStats():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image =  pygame.image.load('images/lifebar.bmp')
        self.life_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

    def draw_lifebar(self):
        for n in range(0,self.ships_left):
            rectangle = self.life_rect
            rectangle[0] = rectangle[3] * n + 20
            self.screen.blit(self.image, rectangle)
