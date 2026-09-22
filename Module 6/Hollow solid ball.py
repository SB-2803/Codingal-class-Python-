import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

#Fill the screen with white colour
screen.fill((255,255,255))
green = (0,255,0)

#Draw solid circle
pygame.draw.circle(screen,green,(300,300),50)

#Draw hollow circle
pygame.draw.circle(screen,green,(100,100),50,3)

#Draw the surface object to the screen
pygame.display.update()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

pygame.quit()