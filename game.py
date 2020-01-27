import pygame
import time
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,ship,screen, aliens)
    pygame.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, bullets,aliens, ship, screen)
        gf. update_aliens(ai_settings, aliens, ship)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        time.sleep(0.001)

run_game()
