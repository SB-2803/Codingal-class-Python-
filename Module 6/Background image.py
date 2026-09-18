import pygame
#Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

#Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image!!')

#Load and scale images directly
bg_image = pygame.transform.scale(
    pygame.image.load('bg.jpg').convert(),(SCREEN_HEIGHT,SCREEN_WIDTH))
penguin_image = pygame.transform.scale(
    pygame.image.load('p.png').convert_alpha(),(250,250))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 - 30))#250,220

#Initialize font,render text and set text position
text = pygame.font.Font(None,36).render('Hello World:)',True,pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 +110))#250,330

#print all supported fonts 
#print(pygame.font.get_fonts())

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(bg_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
    game_loop()