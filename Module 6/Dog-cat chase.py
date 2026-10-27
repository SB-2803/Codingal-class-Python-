import pygame
import random
import math

# Constants
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 300
enemystarty_min = 50
enemystarty_max = 150
enemyspeedx = 4
enemyspeedy = 40
collisiondistance = 20

# Colors
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((screenwidth, screenheight))

# Background
bg = pygame.image.load('bg1.webp')

# Caption and Icon
pygame.display.set_caption("Cat chase")
icon = pygame.image.load('tree.png')
pygame.display.set_icon(icon)

# Player
playerx = playerstartx
playery = playerstarty
playerxchange = 0
playerychange = 0  
playerimg = pygame.image.load('dog.png')
small_image = pygame.transform.scale(playerimg, (50, 50))

# Enemy Initialization
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofenemies = 12

for i in range(numofenemies):
    catimage = pygame.image.load('cat.png')
    small_image1 = pygame.transform.scale(catimage, (50, 50))
    enemyimg.append(small_image1)  # Appends the scaled image
    enemyx.append(random.randint(0, screenwidth - 50))
    enemyy.append(random.randint(enemystarty_min, enemystarty_max))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)

# Score
scorevalue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

# Game Over Font
overfont = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(scorevalue), True, BLACK)
    screen.blit(score, (x, y))

def game_over_text():
    over_text = overfont.render("GAME OVER", True, BLACK)
    screen.blit(over_text, (200, 255))

def player(x, y):
    screen.blit(small_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def isCollision(enemyx_val, enemyy_val):
    # Using ** 2 for squaring values
    distance = math.sqrt((enemyx_val - playerx)**2 + (enemyy_val - playery)**2)
    return distance < collisiondistance

# Game loop setup
running = True
clock = pygame.time.Clock()

while running:
    # RGB background fill and image blit
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
            if event.key == pygame.K_UP:    
                playerychange = -5
            if event.key == pygame.K_DOWN:     
                playerychange = 5

                
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerxchange = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                            playerychange = 0
            

    # Player movement & boundary check
    playerx += playerxchange
    playerx = max(0, min(playerx, screenwidth - 50))
    playery += playerychange
    playery = max(0, min(playery, screenheight - 50))

    # Enemy movement
    for i in range(numofenemies):
        # Game over Condition
        if enemyy[i] > 240:
            for j in range(numofenemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyxchange[i]
        if enemyx[i] <= 0 or enemyx[i] >= screenwidth - 50:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]

        # Collision check
        if isCollision(enemyx[i], enemyy[i]):
            scorevalue += 1  # Increments score when hit
            enemyx[i] = random.randint(0, screenwidth - 50)
            enemyy[i] = random.randint(enemystarty_min, enemystarty_max)

        enemy(enemyx[i], enemyy[i], i)

    player(playerx, playery)
    show_score(textx, texty)
    
    pygame.display.update()
    clock.tick(60)  # Keep the game running at a smooth 60 FPS

pygame.quit()
