import pygame
import time
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from record import Record

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,ship,screen, aliens)
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings, screen)
    record = Record(screen, ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    tick = pygame.time.Clock()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, record)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button,stats, sb, record)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, bullets,aliens, ship, screen, stats, sb)
            gf.update_aliens(ai_settings, aliens, ship, bullets, stats, screen)
        tick.tick(200)



run_game()
