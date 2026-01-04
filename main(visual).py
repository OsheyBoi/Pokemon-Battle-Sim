import time
import random
import pygame
global state, pokemon, yourpokemon

state = 0
yourHealth = 25
opponentHealth = 25
Defence = 1
opponentDefence = 1


pygame.init()
screen = pygame.display.set_mode((520,270))
clock = pygame.time.Clock()
show_popup = True #Flag to control the pop up
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)
font = pygame.font.SysFont("Arial", 24)
background_img = pygame.image.load("selction.png").convert()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if state == 1:
                if event.key == pygame.K_4:
                    yourpokemon = "Treeko"
                    pokemon =  1 #toggle
                    state = 2
                    background_img = pygame.image.load("back.png").convert()
                if event.key == pygame.K_5:
                    yourpokemon = "Oshawott"
                    pokemon =  2 #toggle
                    state = 2
                    background_img = pygame.image.load("back.png").convert()
                    print("test")
                if event.key == pygame.K_6:
                    yourpokemon = "Litten"
                    pokemon =  3 #toggle
                    state = 2
                    background_img = pygame.image.load("back.png").convert()
    if show_popup:
        #popup_surf = pygame.surface((512, 200))
        screen.blit(background_img, (0,0)) #Cords
    pygame.display.flip()
clock.tick(60)
state = 1 # 1 - Selction / 2 - Battle / 3 - Won / 4 - Loss
print(state)
while state == 1:
    time.sleep(1)
background_img = pygame.image.load("back.png").convert()




#yourpokemon_img = pygame.image.load(pokemon+".png").convert_alpha()
#screen.blit(popup_img, (0, 0))