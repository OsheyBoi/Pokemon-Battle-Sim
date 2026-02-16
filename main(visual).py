import random
import pygame
global state, pokemon, yourpokemon, battlestate, attackmsg
global ui_img, rival_img, player_img, background_img
pygame.init()

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

white = (255, 255, 255)
blue = (50, 150, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
black = (0, 0, 0)
X = 400
Y = 400
font = pygame.font.SysFont('Chalkboard.ttf', 64)

text1 = font.render('', True, black, )
text2 = font.render('', True, black, )
text3 = font.render('', True, black, )

ui_img = pygame.image.load("selection.png").convert_alpha()
resized_ui = pygame.transform.scale(ui_img, (1000, 700))

player_img = pygame.image.load("nothing.png").convert_alpha()
resized_player = pygame.transform.scale(player_img, (200, 200))

rival_img = pygame.image.load("nothing.png").convert_alpha()
resized_rival = pygame.transform.scale(rival_img, (200, 200))

background_img = pygame.image.load("back.png").convert()
resized_background = pygame.transform.scale(background_img, (1000, 700))


playerHp_img = pygame.image.load("nothing.png").convert_alpha()
rivalHp_img = pygame.image.load("nothing.png").convert_alpha()
pygame.display.set_caption('Pokemon Battle Sim')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if state == 1:
                if event.key == pygame.K_4:
                    yourpokemon = "Treeko"
                    yourmoves = ["Scratch", "Absorb", "Tail whip"]
                    pokemon = 1  # toggle
                    opponentpokemon = "litten"
                    state = 2
                    print("P1")
                    background_img = pygame.image.load("back.png").convert_alpha()

                if event.key == pygame.K_5:
                    yourpokemon = "Oshawott"
                    yourmoves = ["Tackle", "Water Gun", "Tail whip"]
                    pokemon = 2  # toggle
                    opponentpokemon = "Treeko"
                    state = 2
                    print("P2")

                if event.key == pygame.K_6:
                    yourpokemon = "Litten"
                    yourmoves = ["Tackle", "Ember", "Tail whip"]
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
                    attackmsg = (yourpokemon + " used " + yourmoves[0])
                    opponentHealth = opponentHealth - 5 * opponentDefence
                    display_until = pygame.time.get_ticks() + 3000


                if event.key == pygame.K_2:
                    battlestate = 2
                    playermove = 2
                    attackmsg = (yourpokemon + " used " + yourmoves[1])
                    opponentHealth = opponentHealth - 3 * opponentDefence
                    display_until = pygame.time.get_ticks() + 3000

                if event.key == pygame.K_3:
                    battlestate = 2
                    playermove = 3
                    attackmsg = (yourpokemon + " used " + yourmoves[2])
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

        playerHp_img = pygame.image.load("Hp2.png").convert_alpha()
        text1 = font.render(yourpokemon, True, black, )

        rivalHp_img = pygame.image.load("Hp1.png").convert_alpha()
        text2 = font.render(opponentpokemon, True, black,)

        if battlestate == 1:
            text3 = font.render('Select Your Move', True, black, )

            ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()
            resized_ui = pygame.transform.scale(ui_img, (1000, 200))
        elif battlestate == 2:
            text3 = font.render(attackmsg, True, black, )
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
    screen.blit(playerHp_img, (0, 270))
    screen.blit(rivalHp_img, (0 , 0))
    screen.blit(text1, (750, 300))
    screen.blit(text2, (100, 20))
    if state == 1:
        screen.blit(resized_ui, (0, 00))
    if state == 2:
        screen.blit(resized_ui, (0, 500))
        resized_ui = pygame.transform.scale(ui_img, (1000, 200))
        pygame.draw.rect(screen, black, (670, 370, 310, 60))
        pygame.draw.rect(screen, green, (675, 375, yourHealth * 12 , 50))
        pygame.draw.rect(screen, black, (20, 85, 310, 60))
        pygame.draw.rect(screen, green, (25, 90, opponentHealth * 12 , 50))
    if battlestate == 1:
        screen.blit(text3, (75, 575))
    elif battlestate == 2:
      screen.blit(text3, (300, 575))

    pygame.display.flip()
clock.tick(60)
# state machine continues below


# yourpokemon_img = pygame.image.load(pokemon+".png").convert_alpha()
# screen.blit(popup_img, (0, 0))


