#Import necessary changes
import pygame

#Initialize required modules
pygame.init()

#setup window geometry
screen = pygame.display.set_mode((400,500))

#Create a loop to run till the game is quit by the user
while True:
    #Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #Make the changes visible
    pygame.display.flip()