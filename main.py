import random
from ctypes.macholib.dyld import dyld_executable_path_search

import pygame
import time
global state, pokemon, yourpokemon, battlestate, attackmsg, yourHealth, Defence, ui_img, rival_img, player_img, background_img, Dex
pygame.init()
# Set the base of each variable
state = 1  # 1 - Selection / 2 - Battle / 3 - Won / 4 - Loss
yourHealth = 30
display_until = 1
current_time = 1
opponentHealth = 30
Defence = 1
opponentDefence = 1
battlestate = 1
attackmsg = "na"

def Attack(Damage):
    min = Damage - 1
    max = Damage + 1
    Damage = random.randint(min,max)
    return Damage


pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
show_popup = True

# Colour and text System
white = (255, 255, 255)
blue = (50, 150, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
black = (0, 0, 0)
X = 400
Y = 400
font = pygame.font.SysFont('Chalkboard.ptf', 64)

text1 = font.render('', True, black, )
text2 = font.render('', True, black, )
text3 = font.render('', True, black, )

# Image loading (State 1)
ui_img = pygame.image.load("selection.png").convert_alpha()
resized_ui = pygame.transform.scale(ui_img, (1000, 700))

player_img = pygame.image.load("nothing.png").convert_alpha()
resized_player = pygame.transform.scale(player_img, (225, 225))

rival_img = pygame.image.load("nothing.png").convert_alpha()
resized_rival = pygame.transform.scale(rival_img, (225, 225))

background_img = pygame.image.load("back.png").convert()
resized_background = pygame.transform.scale(background_img, (1000, 700))

playerHp_img = pygame.image.load("nothing.png").convert_alpha()
rivalHp_img = pygame.image.load("nothing.png").convert_alpha()
pygame.display.set_caption('Pokemon Battle Sim')

program_img = pygame.image.load("Logo.png")
pygame.display.set_icon(program_img)

# Music
pygame.mixer.music.load("Theme.ogg")

# Dex and Moves
Dex = {
    "Treeko" : ["Scratch", "Absorb", "Tail whip"],
    "Littens" : ["Tackle", "Ember", "Tail whip"],
    "Oshawott" : ["Tackle", "Water Gun", "Tail whip"]
}
#Running of games
running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # starter selection
            if state == 1:
                if event.key == pygame.K_4:
                    yourpokemon = "Treeko"
                    pokemon = 1  # toggle
                    opponentpokemon = "Litten"
                    state = 2
                    print("P1")
                    pygame.mixer.music.play(loops=10)

                if event.key == pygame.K_5:
                    yourpokemon = "Oshawott"
                    pokemon = 2  # toggle
                    opponentpokemon = "Treeko"
                    state = 2
                    print("P2")
                    pygame.mixer.music.play(loops=10)

                if event.key == pygame.K_6:
                    yourpokemon = "Litten"
                    pokemon = 3  # toggle
                    opponentpokemon = "Oshawott"
                    state = 2
                    print("P3")
                    pygame.mixer.music.play(loops=10)

            # Move Selection
            elif state == 2:
                if battlestate == 1 and current_time > display_until:
                    print("Loaded State 2")
                    moveused = 0
                    Base = 5 # Base Damage

                    if event.key == pygame.K_1:
                        playermove = 0
                        damage = Attack(Base)
                        opponentHealth = opponentHealth - damage  * opponentDefence
                        moveused = 1
                    if event.key == pygame.K_2:
                        playermove = 1
                        damage = Attack(Base)
                        opponentHealth = opponentHealth - damage * opponentDefence / 2
                        moveused = 1

                    if event.key == pygame.K_3:
                        playermove = 3
                        opponentDefence = opponentDefence + 0.3
                        moveused = 1

                    if moveused == 1:
                        move = (Dex)[yourpokemon][playermove]
                        attackmsg = (yourpokemon + " used " + move)
                        moveused = 1
                        battlestate = 2
                        ui_img = pygame.image.load("Textbox.png").convert_alpha()
                        display_until = current_time + 1500
        # Quit once win/lose
        if state >= 3:
            if event.key == pygame.K_SPACE:
                quit()

    if state == 2:
        # Ai Attack
        if battlestate == 2 and current_time > display_until:
            Ai_move = (random.randint(1, 3))
            print(Ai_move)
            base = 5
            if Ai_move == 1:
                attackmsg = (opponentpokemon + " used " + rivalmoves[0])
                damage = Attack(Base)
                yourHealth = yourHealth - damage * Defence
                print("aimoveused")


            if Ai_move == 2:
                attackmsg = (opponentpokemon + " used " + rivalmoves[1])
                damage = Attack(Base)
                yourHealth = yourHealth - damage * Defence * 2
                print("aimoveused")


            if Ai_move == 3:
                attackmsg = (opponentpokemon + " used " + rivalmoves[2])
                Defence = Defence + 0.3
                print("aimoveused")

            display_until = current_time + 1500
            battlestate = 3
        #Disable Textbox
        if battlestate == 3 and current_time > display_until:
            battlestate = 1
            ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()




    if state == 2:
        #image loader (State 2)
        screen.fill((0, 0, 0))
        background_img = pygame.image.load("back.png").convert_alpha()
        player_img = pygame.image.load(str(yourpokemon) + " front.png").convert_alpha()
        rival_img = pygame.image.load(str(opponentpokemon) + " back.png").convert_alpha()

        #Incressed Image size
        resized_background = pygame.transform.scale(background_img, (1000, 700))
        resized_player = pygame.transform.scale(player_img, (200, 200))
        resized_rival = pygame.transform.scale(rival_img, (200, 200))

        # HP Bars (1 - Rival, 2 - Player)
        playerHp_img = pygame.image.load("Hp2.png").convert_alpha()
        text1 = font.render(yourpokemon, True, black, )

        rivalHp_img = pygame.image.load("Hp1.png").convert_alpha()
        text2 = font.render(opponentpokemon, True, black,)

        # Winner or loser Screen Updater
        if state == 3:
            ui_img = pygame.image.load("nothing.png").convert_alpha()
            player_img = pygame.image.load("nothing.png").convert_alpha()
            rival_img = pygame.image.load("nothing.png").convert_alpha()
            background_img = pygame.image.load("Winner.png").convert()
        if state == 4:
            ui_img = pygame.image.load("nothing.png").convert_alpha()
            player_img = pygame.image.load("nothing.png").convert_alpha()
            rival_img = pygame.image.load("nothing.png").convert_alpha()
            background_img = pygame.image.load("Loser.png").convert()
    # Textbox Updater
    if state  == 2:
        if battlestate == 1:
            ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()

        elif battlestate == 2 or 3 :
            ui_img = pygame.image.load("Textbox.png").convert_alpha()
    #Location of text/sprite
    screen.blit(resized_background, (0, 0))
    screen.blit(resized_ui, (0, 500))
    screen.blit(resized_player, (40, 280))
    screen.blit(resized_rival, (700,60 ))
    screen.blit(playerHp_img, (0, 270))
    screen.blit(rivalHp_img, (0 , 0))
    screen.blit(text1, (715, 310))
    screen.blit(text2, (95, 40))

    if state == 1:
        screen.blit(resized_ui, (0, 0))
        text3 = font.render("Select your Pokemon", True, black,)

    if state == 2:
        # HP Bar Drawing
        BAR_HEIGHT = 50
        CURVE_RADIUS = BAR_HEIGHT // 2
        screen.blit(resized_ui, (0, 500))
        resized_ui = pygame.transform.scale(ui_img, (1000, 200))
        pygame.draw.rect(screen, black, (670, 370, 310, 60), border_radius=30)
        pygame.draw.rect(screen, green, (675, 375, yourHealth * 10 , BAR_HEIGHT), border_radius=CURVE_RADIUS)
        pygame.draw.rect(screen, black, (20, 85, 310, 60), border_radius=30)
        pygame.draw.rect(screen, green, (25, 90, opponentHealth * 10, BAR_HEIGHT), border_radius=CURVE_RADIUS)
        msg = attackmsg if battlestate > 1 else ("Select Move (1,2,3)")
        text3 = font.render(msg, True, black,)

    if state == 1:
        screen.blit(text3, (250, 70))

    if state == 2:
        if battlestate == 1:
            screen.blit(text3, (75, 575))
        elif battlestate >= 2:
          screen.blit(text3, (300, 575))
    # Set to win or lose

    if opponentHealth <= 0:
        state = 3

    if yourHealth <= 0:
        state = 4

    pygame.display.flip()
clock.tick(60)


