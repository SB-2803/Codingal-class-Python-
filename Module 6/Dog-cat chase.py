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
small_image = pygame.transform.scale(playerimg, (50, 50))
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
    catimage = pygame.image.load("cat.png")
    enemyimg.append(catimage)
    small_image1 = pygame.transform.scale(catimage, (50, 50))
    enemyx.append(random.randint(0,screenwidth - 50))
    enemyy.append(random.randint(enemystarty_min,enemystarty_max))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)

#score 
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10

#Game over font
overfont = pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    #Display the current score on the screen.
    score = font.render("Score:" + str(scorevalue), True,'black')
    screen.blit(score, (x,y))

def game_over_text():
    #display the game over text
    over_text = over_text.render("GAME OVER",True,'black')
    screen.blit(over_text, (200,255))

def player(x,y):
    screen.blit(small_image, (x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def isCollision(enemyx, enemyy,):
    #Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyx - playerx) ** 2 + (enemyy - playery) ** 2)
    return distance < collisiondistance

#game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
        if event.type == pygame.KEYUP and event.key in[pygame.K_LEFT, pygame.K_RIGHT]:
            playerxchange = 0

    #player movement
    playerx += playerxchange
    playerx = max(0,min(playerx,screenwidth-64))

    #enemy movement
    for i in range(numofenemies):
        if enemyy[i] > 340: #Game over Condition
            for j in range(numofenemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyxchange[i]
        if enemyx[i] <= 0 or enemyx[i] >= screenwidth - 64:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]

        #Collision check
        if isCollision(enemyx[i], enemyy[i]):
            enemyx[i] = random.randint(0, screenwidth - 64)
            enemyy[i] = random.randint(enemystarty_min, enemystarty_max)

        enemy(enemyx[i], enemyy[i], i)

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()