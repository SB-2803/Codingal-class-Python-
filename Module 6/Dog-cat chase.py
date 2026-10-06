import pygame
import random
import math

#Constants
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 300
enemystarty_min = 50
enemystarty_max = 150
enemyspeedx = 4
enemyspeedy = 40
collisiondistance = 20

pygame.init()
screen = pygame.display.set_mode((screenwidth,screenheight))

#background
bg = pygame.image.load('bghw.jpg')

#caption and icon
pygame.display.set_caption("Cat chase!!")
icon = pygame.image.load("tree.png")
pygame.display.set_icon(icon)

#player
playerx = playerstartx
playerimg = pygame.image.load("dog.png")
playery = playerstarty
playerxchange = 0

#enemy
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofenemies = 7

for i in range(numofenemies):
    enemyimg.append(pygame.image.load("cat.png"))
    enemyx.append(random.randint(0,screenwidth - 64))
    enemyy.append(random.randint(enemystarty_min,enemystarty_max))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)

#score 
scorevalue = 0
font = pygame.font.Font("Comic Sans MS",32)
textx = 10
texty = 10

#Game over font
overfont = pygame.font.Font("Comic Sans MS",64)

def show_score(x,y):
    #Display the current score on the screen.
    score = font.render("Score:", scorevalue, True,'black')
    screen.blit(score, (x,y))

def game_over_text():
    #display the game over text
    over_text = over_text.render("GAME OVER",True,'black')
    screen.blit(over_text, (200,255))

def player(x,y):
    screen.blit(playerimg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

print(pygame.font.get_fonts())