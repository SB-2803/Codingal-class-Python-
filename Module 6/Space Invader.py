import pygame
import random
import math

#Constants
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 380
enemystarty_min = 50
enemystarty_max = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 20

pygame.init()
screen = pygame.display.set_mode((screenwidth,screenheight))

#background
bg = pygame.image.load('space_bg.png')

#caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player
playerx = playerstartx
playerimg = pygame.image.load("player.png")
playery = playerstarty
playerxchange = 0

#enemy
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofenemies = 6

for i in range(numofenemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,screenwidth - 64))
    enemyy.append(random.randint(enemystarty_min,enemystarty_max))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)

#Bullet
bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = playerstarty
bulletychange = bulletspeedy
bulletstate = "ready"

#score 
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10

#Game over font
overfont = pygame.font.Font("freesansbold.ttf",64) #enemy's width is 64

def show_score(x,y):
    #Display the current score on the screen.
    score = font.render("Score:", scorevalue, True,'white')
    screen.blit(score, (x,y))

def game_over_text():
    #display the game over text
    over_text = overfont.render("GAME OVER",True,'white')
    screen.blit(over_text, (200,255))

def player(x,y):
    screen.blit(playerimg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg,(x+16, y+10))

def isCollision(enemyx, enemyy, bulletx, bullety):
    #Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy + bullety) ** 2)
    return distance < collisiondistance

#game loop
running = True
while running:
    screen.fill((0,0,0,))
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerxchange = -5
            if event.type == pygame.K_RIGHT:
                playerxchange = 5
            if event.type == pygame.K_SPACE and bulletstate == "ready":
                bulletx = playerx
                fire_bullet(bulletx,bullety)
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
        if isCollision(enemyx[i], enemyy[i], bulletx, bullety):
            bullety = playerstarty
            bulletstate = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, screenwidth - 64)
            enemyy[i] = random.randint(enemystarty_min, enemystarty_max)

        enemy(enemyx[i], enemyy[i], i)

    #Bullet movement
    if bullety <= 0:
        bullety = playerstarty
        bulletstate = "ready"
    elif bulletstate == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bulletychange

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()