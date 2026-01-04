import pygame
pygame.init()
screen = pygame.display.set_mode((520,270))
clock = pygame.time.Clock()
show_popup = True #Flag to control the pop up
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)
font = pygame.font.SysFont("Arial", 24)
background_img = pygame.image.load("back.png").convert()
popup_img = pygame.image.load("Treeko.png").convert_alpha()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_popup = not show_popup #toggle
    if show_popup:
        #popup_surf = pygame.surface((512, 200))
        screen.blit(background_img, (0,0))
        screen.blit(popup_img, (0, 0)) #Cords
    pygame.display.flip()
clock.tick(60)