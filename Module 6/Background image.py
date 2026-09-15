import pygame
#Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
#Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Load and scale images directly
bg_image = pygame.transform.scale(
    pygame.image.load('bg.png').convert(),(SCREEN_HEIGHT,SCREEN_WIDTH))
penguin_image = pygame.transform.scale(
    pygame.image.load('p.png').convert_alpha(),(200,200))