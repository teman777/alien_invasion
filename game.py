import pygame
import time
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button,stats, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, bullets,aliens, ship, screen, stats, sb)
            gf.update_aliens(ai_settings, aliens, ship, bullets, stats, screen)

        time.sleep(0.001)


run_game()
