import random
import pygame
global state, pokemon, yourpokemon, battlestate
global ui_img, rival_img, player_img, background_img

state = 1  # 1 - Selection / 2 - Battle / 3 - Won / 4 - Loss
yourHealth = 25
opponentHealth = 25
Defence = 1
opponentDefence = 1
battlestate = 1

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
show_popup = True  # Flag to control the pop up
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)
font = pygame.font.SysFont("Arial", 24)
ui_img = pygame.image.load("nothing.png").convert_alpha()
resized_ui = pygame.transform.scale(ui_img, (1000, 200))
player_img = pygame.image.load("nothing.png").convert_alpha()
resized_player = pygame.transform.scale(player_img, (200, 200))
rival_img = pygame.image.load("nothing.png").convert_alpha()
resized_rival = pygame.transform.scale(rival_img, (200, 200))
background_img = pygame.image.load("selction.png").convert()
resized_background = pygame.transform.scale(background_img, (1000, 700))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if state == 1:
                if event.key == pygame.K_4:
                    yourpokemon = "Treeko"
                    pokemon = 1  # toggle
                    opponentpokemon = "litten"
                    state = 2
                    print("P1")
                if event.key == pygame.K_5:
                    yourpokemon = "Oshawott"
                    yourmoves = ["Tackle", "Water Gun", "Tail whip"]
                    pokemon = 2  # toggle
                    opponentpokemon = "Treeko"
                    state = 2
                    print("P2")
                if event.key == pygame.K_6:
                    yourpokemon = "Litten"
                    pokemon = 3  # toggle
                    opponentpokemon = "Oshawott"
                    state = 2
                    print("P3")
            elif state == 2 and battlestate == 1:
                print("Loaded State 2")
                print("1")
                if event.key == pygame.K_1:
                    battlestate = 2
                    playermove = 1
                    print("Player used " + yourmoves[0])
                    opponentHealth = opponentHealth - 5 * opponentDefence
                    display_until = pygame.time.get_ticks() + 3000
                if event.key == pygame.K_2:
                    battlestate = 2
                    playermove = 2
                    print("Player used " + yourmoves[1])
                    opponentHealth = opponentHealth - 3 * opponentDefence
                    display_until = pygame.time.get_ticks() + 3000
                if event.key == pygame.K_3:
                    battlestate = 2
                    playermove = 3
                    print("Player used " + yourmoves[2])
                    opponentDefence = opponentDefence + 0.3
                    display_until = pygame.time.get_ticks() + 3000
            elif state == 3:
                if event.key == pygame.K_SPACE:
                    quit()
    if state == 2:
        screen.fill((0, 0, 0))
        background_img = pygame.image.load("back.png").convert_alpha()
        player_img = pygame.image.load(str(yourpokemon) + " front.png").convert_alpha()
        rival_img = pygame.image.load(str(opponentpokemon) + " back.png").convert_alpha()
        resized_background = pygame.transform.scale(background_img, (1000, 700))
        resized_player = pygame.transform.scale(player_img, (200, 200))
        resized_rival = pygame.transform.scale(rival_img, (200, 200))
        if battlestate == 1:
            screen.fill((0, 0, 0))
            ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()
            resized_ui = pygame.transform.scale(ui_img, (1000, 200))
        elif battlestate == 2:
            screen.fill((0, 0, 0))
            ui_img = pygame.image.load("Textbox.png").convert_alpha()
            resized_ui = pygame.transform.scale(ui_img, (1000, 200))
            if battlestate == 2 and pygame.time.get_ticks() > display_until:
                battlestate = 1
                if opponentHealth <= 0:
                    state = 3
        if state == 3:
            ui_img = pygame.image.load("nothing.png").convert_alpha()
            player_img = pygame.image.load("nothing.png").convert_alpha()
            rival_img = pygame.image.load("nothing.png").convert_alpha()
            background_img = pygame.image.load("Winner.png").convert()

    screen.blit(resized_background, (0, 0))
    screen.blit(resized_ui, (0, 500))
    screen.blit(resized_player, (40, 280))
    screen.blit(resized_rival, (700,60 ))
    pygame.display.flip()
clock.tick(60)
# state machine continues below


# yourpokemon_img = pygame.image.load(pokemon+".png").convert_alpha()
# screen.blit(popup_img, (0, 0))


