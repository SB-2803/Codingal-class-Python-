import pygame
import random

pygame.init()

#Custom event IDs for colour change events
spritecolourchangeevent = pygame.USEREVENT + 1
bgcolourchangeevent = pygame.USEREVENT + 2

#bg colours
blue = pygame.Color('blue')
lightblue = pygame.Color('lightblue')
aqua = pygame.Color('aqua')
aquamarine = pygame.Color('aquamarine')

#sprite colours
yellow = pygame.Color('yellow')
salmon = pygame.Color('lightsalmon2')
magenta = pygame.Color('magenta')
white = pygame.Color('white')

#Creating a group
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Colourful Bounce!!")
bgcolour = blue
screen.fill(bgcolour)

exit = True
clock = pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == spritecolourchangeevent:
            sp1.change_color()
        elif event.type == bgcolourchangeevent:
                    change_bg_colour()

    all_sprites_list.update()
    screen.fill(bgcolour)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()