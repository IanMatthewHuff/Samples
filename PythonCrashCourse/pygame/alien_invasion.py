import sys
import pygame

# from pygame.locals import *

# from pygame.constants import (
    # MOUSEBUTTONDOWN, QUIT, MOUSEMOTION, KEYDOWN
# )

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # Start the main game loop
    while True:

        # Watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()