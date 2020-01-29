import pygame.font


class Record():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.load_record()
        self.create_image()



    def load_record(self):
        with open("data/record.txt", "r") as f:
            self.record = int(f.read())
        if self.record is None:
            self.record = 0

    def save_record(self, record):
        self.record = record
        with open("data/record.txt", "w") as f:
            f.write(str(self.record))

    def create_image(self):
        self.record_image = self.font.render(str(self.record), True, self.text_color, self.ai_settings.bg_color)
        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.top = 20

    def draw(self):
        self.create_image()
        self.screen.blit(self.record_image, self.record_rect)
