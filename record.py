import pygame


class Record():

    def __init__(self, screen):
        self.screen = screen
        
            
    def load_record(self):
        with open("data/record.txt", "r") as f:
            self.record = int(f.read())
        if self.record is None:
            self.record = 0

    def save_record(self, record):
        self.record = record
        with open("data/record.txt", "w") as f:
            f.write(self.record)

    def draw(self, screen):
       self.screen.blit(self.image, self.rect)
