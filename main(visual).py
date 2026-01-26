import time
import random
import pygame
global state, pokemon, yourpokemon, battlestate
global ui_img,rival_img,player_img,background_img

state = 1  # 1 - Selection / 2 - Battle / 3 - Won / 4 - Loss
yourHealth = 25
opponentHealth = 25
Defence = 1
opponentDefence = 1
battlestate = 1

pygame.init()
screen = pygame.display.set_mode((520,280))
clock = pygame.time.Clock()
show_popup = True #Flag to control the pop up
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)
font = pygame.font.SysFont("Arial", 24)
ui_img = pygame.image.load("nothing.png").convert_alpha()
player_img = pygame.image.load("nothing.png").convert_alpha()
rival_img = pygame.image.load("nothing.png").convert_alpha()
background_img = pygame.image.load("selction.png").convert()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = True
            if event.key == pygame.K_0:
                print("Test")
                print (state)
                print ("Background - " + str(background_img))
                print("Ui - "+ str(ui_img))
                print("Player - " + (player_img))
                print("Rival - " + str(rival_img))
                if state == 1:
                    if event.key == pygame.K_4:
                            yourpokemon = "Treeko"
                            pokemon =  1 #toggle
                            opponentpokemon = "litten"
                            state = 2
                    if event.key == pygame.K_5:
                            yourpokemon = "Oshawott"
                            pokemon=  2 #toggle
                            opponentpokemon = "Treeko"
                            state = 2
                            print(state)
                    if event.key == pygame.K_6:
                            yourpokemon = "Litten"
                            pokemon =  3 #toggle
                            opponentpokemon = "Oshawott"
                            state = 2
                elif state == 2 and battlestate == 1:
                    print ("Loaded State 2")
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                        battlestate = 2
                                        playermove = 1
                                        print ("Player used move 1")
                            if event.key == pygame.K_2:
                                        battlestate = 2
                                        playermove = 2
                                        print ("Player used move 2")
                            if event.key == pygame.K_3:
                                        battlestate = 2
                                        playermove = 3
                                        print ("Player used move 3")
    if state == 2:
        screen.fill((0,0,0))
        background_img = pygame.image.load("back.png").convert_alpha()
        player_img = pygame.image.load(str(yourpokemon)+".png").convert_alpha()
        rival_img = pygame.image.load(str(opponentpokemon)+".png").convert_alpha()
    
    
    #ui_img = pygame.image.load("Textbox.png").convert_alpha()
    #ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()
    screen.blit(background_img, (0,0))
    screen.blit(ui_img, (0,0)) 
    screen.blit(player_img, (-150, -150)) 
    screen.blit(rival_img, (150,150)) 
    pygame.display.flip()
clock.tick(60)
# state machine continues below




#yourpokemon_img = pygame.image.load(pokemon+".png").convert_alpha()
#screen.blit(popup_img, (0, 0))


