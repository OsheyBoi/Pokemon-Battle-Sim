import random
from bdb import effective
from tkinter.constants import NORMAL
import pygame
import time
global state, pokemon, yourpokemon, battlestate, attackmsg, yourHealth, Defence, ui_img, rival_img, player_img, background_img, Dex
global playermove, Type, rivalType, resized_background
# Set the base of each variable
state = 0  # 1 - Selection / 2 - Battle / 3 - Won / 4 - Loss
yourHealth = 40
display_until = 1
current_time = 1
opponentHealth = 40
Defence = 1.0
opponentDefence = 1.0
battlestate = 1
effectiveness = 1
Fade = 0
FadeSpeed = 3
attackmsg = "na"

#Attack Damage
def Attack():
    Damage = random.randint(3,7)
    return Damage

# Effictiveness Checker
def Typedex(movetype,oppenenttype):
    Weakwater = ["Water", "Grass","Dragon"]
    Strongwater = ["Fire", "Rock", "Ground"]
    Weakfire = ["Fire", "Water","Rock", "Dragon"]
    Strongfire = ["Grass", "Ice", "Bug", "Steel"]
    Reallystronggrass = ["Water/Rock"]
    Weakgrass = ["Fire", "Grass", "Dragon"]
    Stronggrass = ["Water", "Ground", "Rock"]
    ImmuneElectric = ["Ground"]
    WeakElectric = ["Dragon, Electric", "Grass"]
    StorngElectric = ["Flying", "Water", 'Water/Rock']
    ImmuneNormal = ["Ghost"]
    WeakNormal = ["Rock", "Steel"]
    StrongFairy = ["Fighting", "Dragon", "Dark"]
    WeakFariy = ["Fire","Poison", "Steel"]
    StrongFairy = ["Fighting", "Dragon", "Dark"]
    WeakFariy = ["Fire","Poison", "Steel"]
    #Weak = ["", "", "", ""]
    #Strong = ["", "", "", ""]
    Effectiveness = 1


    if movetype == "Water":
        if oppenenttype in Weakwater:
            Effectiveness = 0.5
        if oppenenttype in Strongwater:
            Effectiveness = 2
    if movetype == "Fire":
        if oppenenttype in Weakfire:
            Effectiveness = 0.5
        if oppenenttype in Strongfire:
            Effectiveness = 2
    if movetype == "Grass":
        if oppenenttype in Weakgrass:
            Effectiveness = 0.5
        if oppenenttype in Stronggrass:
            Effectiveness = 2
        if oppenenttype in Reallystronggrass:
            Effectiveness = 4
    if movetype == "Normal":
        if oppenenttype in ImmuneNormal:
            Effectiveness = 0
        if oppenenttype in WeakNormal:
            Effectiveness = 0.5
    if movetype == "Electric":
        if oppenenttype in ImmuneElectric:
            Effectiveness = 0
        if oppenenttype in WeakElectric:
            Effectiveness = 0.5
        if oppenenttype in StorngElectric:
            Effectiveness = 2
    if movetype == "Fairy":
        if oppenenttype in WeakFariy:
            Effectiveness = 0.5
        if oppenenttype in StrongFairy:
            Effectiveness = 2
    return Effectiveness

def PokemonSelction(Pokemon):
    Dex = ["Treeko", "Oshawott", "Litten", "Pikachu", "Eevee", "Snubbull", "Kabuto"]
    Selctedpokemon = Dex[Pokemon]
    return Selctedpokemon

def PokemonType(Pokemon):
    Types = ["Grass","Water","Fire", "Electric", "Normal", "Fairy", "Water/Rock"]
    Type = Types[Pokemon]
    return Type

def Movetype(move,Usertype):
    a = 0
    # For Kabuto
    if Usertype == "Water/Rock" :
        Usertype = "Water"

    if move == 0:
        Type = 'Normal'
        a = 1
    if move == 1:
        Type = Usertype
        a = 1
    if a == 1:
        return Type

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
ui_img = pygame.image.load("Name.png")
resized_ui = pygame.transform.scale(ui_img, (1000, 700))

player_img = pygame.image.load("nothing.png").convert_alpha()
resized_player = pygame.transform.scale(player_img, (270, 270))

rival_img = pygame.image.load("nothing.png").convert_alpha()
resized_rival = pygame.transform.scale(rival_img, (270, 270))

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
    "Litten" : ["Tackle", "Ember", "Tail whip"],
    "Oshawott" : ["Tackle", "Water Gun", "Tail whip"],
    "Pikachu" : ["Tackle", "Thunder Shock", "Tail Whip"],
    "Eevee": ["Tackle", "Quick Attack", "Tail Whip"],
    "Snubbull": ["Tackle", "Play Rough", "Tail Whip"],
    "Kabuto": ["Scratch", "Water Gun", "Leer"]
}
#Running of games
running = True
while running:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            # starter selection
            if state == 1:
                pokemon = -1
                if event.key == pygame.K_q:
                    pokemon = 0
                    print ("1")
                if event.key == pygame.K_w:
                    pokemon = 1  # toggle
                    print ("2")
                if event.key == pygame.K_e:
                    pokemon = 2  # toggle
                    print ("3")
                if event.key == pygame.K_r:
                    pokemon = 3  # toggle
                    print ("4")
                if event.key == pygame.K_t:
                    pokemon = 4  # toggle
                    print ("5")
                if event.key == pygame.K_y:
                    pokemon = 5  # toggle
                    print ("6")
                if event.key == pygame.K_u:
                    pokemon = 6  # toggle
                    print ("7")

                if pokemon >= 0:
                    print ("Checking")
                    yourpokemon = PokemonSelction(pokemon)
                    Type = PokemonType(pokemon)
                    #Auto Rival Pokemon Selector
                    rivalnumber = random.randint(0,6)
                    opponentpokemon = PokemonSelction(rivalnumber)
                    rivalType = PokemonType(rivalnumber)


                    print (yourpokemon + " : " + Type)
                    state = 2
                    pygame.mixer.music.play(loops=10)

            # Move Selection
            elif state == 2:
                if battlestate == 1 and current_time > display_until:
                    print("Loaded State 2")
                    moveused = 0
                    damage = Attack()
                    if event.key == pygame.K_1:
                        damage = Attack()
                        playermove = 0
                        moveused = 1

                    if event.key == pygame.K_2:
                        damage = Attack()
                        playermove = 1
                        moveused = 1


                    if event.key == pygame.K_3:
                        AttackType = "NA"
                        damage = 0
                        playermove = 2
                        opponentDefence = opponentDefence + 0.4
                        moveused = 1

                    #After move selected
                    if moveused == 1:
                        print("Moveused?")
                        if playermove != 2:
                            AttackType = Movetype(playermove, Type)
                            print(rivalType)
                            effectiveness = Typedex(AttackType,rivalType)
                            print(effectiveness)
                            opponentHealth = opponentHealth - damage * opponentDefence * effectiveness
                        else :
                            Attacktype = "NA"
                            print('Lower Defence')
                        move = (Dex)[yourpokemon][playermove]
                        print("Player:" + move + " : " + str(AttackType) + ' : ' + str(opponentHealth) + " : " + str(effectiveness) )
                        attackmsg = (yourpokemon + " used " + move)
                        moveused = 0
                        battlestate = 2
                        ui_img = pygame.image.load("Textbox.png").convert_alpha()
                        display_until = current_time + 1500
                        print("skip")
        # Quit once win/lose
        if state >= 3:
            if event.key == pygame.K_SPACE:
                quit()
    if state == 2:
        # Ai Attack
        if battlestate == 2 and current_time > display_until:
            Ai_move = (random.randint(0, 2))
            print(Ai_move)
            damage = Attack()

            if Ai_move == 0 or 1:
                moveused = 1

            if Ai_move == 2:
                AttackType = "NA"
                damage = 0
                Defence = Defence + 0.4
                moveused = 1

            if moveused == 1:
                    print("aimoveused")
                    if Ai_move != 2:
                        AttackType = Movetype(Ai_move, rivalType)
                        effectiveness = Typedex(AttackType,Type)
                        yourHealth = yourHealth - damage * Defence * effectiveness
                    move2 = (Dex)[opponentpokemon][Ai_move]
                    print(move2 + " : " + str(AttackType) + ' : ' +  str(yourHealth) +  " : " + str(effectiveness))
                    attackmsg = (opponentpokemon + " used " + move2)
                    display_until = current_time + 1500
                    battlestate = 3
                    moveused = 0
        #Disable Textbox
        if battlestate == 3 and current_time > display_until:
            battlestate = 1
            ui_img = pygame.image.load("MS" + str(pokemon) + ".png").convert_alpha()





    if state == 0:
        if Fade < 250:
            print (Fade)
            #resized_ui.set_alpha(Fade)
            Fade = Fade + FadeSpeed
        if Fade >= 250:
            print("1")
            state = 1


    if state == 1:
        screen.fill((0, 0, 0))
        resized_ui = pygame.image.load("selection.png").convert_alpha()

    if state == 2:
        #image loader (State 2)
        screen.fill((0, 0, 0))
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
    screen.blit(resized_player, (40, 280))
    screen.blit(resized_rival, (700,60 ))
    screen.blit(playerHp_img, (0, 270))
    screen.blit(rivalHp_img, (0 , 0))
    screen.blit(text1, (715, 310))
    screen.blit(text2, (95, 40))

    if state == 0:
        screen.blit(resized_ui, (0, 0))

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
        pygame.draw.rect(screen, green, (675, 375, yourHealth * 6 , BAR_HEIGHT), border_radius=CURVE_RADIUS)
        pygame.draw.rect(screen, black, (20, 85, 310, 60), border_radius=30)
        pygame.draw.rect(screen, green, (25, 90, opponentHealth * 6, BAR_HEIGHT), border_radius=CURVE_RADIUS)
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


