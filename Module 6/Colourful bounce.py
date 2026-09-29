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

#Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    #Constructor method
    def __init__(self,colour,height,width):
     #Call to the parent class(Sprite) constructor
     super().__init__()
     #Create the sprite's surface with dimensions and colour
     self.image = pygame.Surface([width,height])
     self.image.fill(colour)
     #get the sprite's rect defining its position and size
     self.rect = self.image.get_rect()
     #set initial velocity with random directions
     self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <=0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <=0 or self.rect.bottom >= 400:
                    self.velocity[1] = -self.velocity[1]
                    boundary_hit = True

        if boundary_hit:
             pygame.event.post(pygame.event.Event(spritecolourchangeevent))
             pygame.event.post(pygame.event.Event(bgcolourchangeevent))

    def change_color(self):
        self.image.fill(random.choice([yellow,salmon,magenta,white]))

def change_bg_colour():
    global bgcolour
    bgcolour = random.choice([blue,lightblue,aqua,aquamarine])

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