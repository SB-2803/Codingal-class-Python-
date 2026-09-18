import pygame
#Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

#Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Wildlife information display!!')

#Load and scale images directly
bg_image = pygame.transform.scale(
    pygame.image.load('bag.jpg').convert(),(SCREEN_HEIGHT,SCREEN_WIDTH))
tiger_image = pygame.transform.scale(
    pygame.image.load('t.png').convert_alpha(),(250,250))
tiger_rect = tiger_image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 + 75))#250,325

#Initialize font,render text and set text position
text1 = pygame.font.Font(None,36).render('Tigers are powerful catss',True,pygame.Color('black'))
text_rect1 = text1.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 +220))#250,470
text2 = pygame.font.Font(None,36).render('Save Tigers,Save wildlife!!',True,pygame.Color('black'))
text_rect2 = text2.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 - 100 ))#250,150
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
        display_surface.blit(tiger_image,tiger_rect)
        display_surface.blit(text1,text_rect1)
        display_surface.blit(text2,text_rect2)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__=='__main__':
    game_loop()