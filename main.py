import time
import random
yourHealth = 25
opponentHealth = 25
# starter Pokemon selection
print("Choose a starter:")
print("1. Treecko" " a")
print("2. Oshawott" " b")
print("3. Litten" " c")
a = "Treecko"
b = "Oshawott"
c = "Litten"
Pokemon = input("a, b, or c?")
if Pokemon == "a":
    Pokemon = a  # Your pokemon
    You = ["Scratch", "Absorb", "Tail whip"]  # Your pokemon's moves
    Opponent = c  # Opponent's pokemon
    moves2 = ["Tackle", "Ember", "Tail whip"]  # Opponent's pokemon moves
if Pokemon == "b":
    Pokemon = b
    You = ["Tackle", "Water Gun", "Tail whip"]
    Opponent = a
    moves2 = ["Scratch", "Absorb", "Tail whip"]
if Pokemon == "c":
    Pokemon = c
    You = ["Tackle", "Ember", "tail whip"]
    Opponent = b
    Moves2 = [["Tackle", "Water Gun", "Tail whip"]]
# end starter pokemon selection
# moves
def moves():  # Battle Turn
    global yourHealth
    global opponentHealth
    print(You[0] + " (a)")
    print(You[1] + " (b)")
    print(You[2] + " (c)")
    Attack = input("Move:")  # Your move
    miss = random.randint(0, 10)
    crit = random.randint(0, 10)
    if miss < 8:  # Attact Hit or Miss
        if Attack == "a":
            print(Pokemon + " Used " + You[0])
            if crit == 1:
                opponentHealth = opponentHealth - 8
                print("A Critical Hit!")
            else:
                opponentHealth = opponentHealth - 5
        if Attack == "b":
            print(Pokemon + " Used " + You[1])
            if crit == 1:
                opponentHealth = opponentHealth - 5
                print("A Critical Hit!")
            else:
                opponentHealth = opponentHealth - 3
        if Attack == "c":
            print(Pokemon + " Used " + You[2])
            print("ERROR")
    else:
        print(Pokemon + "'s attack missed!")
def movesopponent():  # Battle Turn
    global yourHealth
    global opponentHealth
    Attack2 = random.randint(1, 3) # Your move
    miss2 = random.randint(0, 10)
    crit2 = random.randint(0, 10)
    if miss2 < 8:  # Attack Hit or Miss
        if Attack2 == 1:
            print(Opponent + " Used " + moves2[0])
            if crit2 == 1:
                yourHealth = yourHealth - 7
                print("A Critical Hit!")
            else:
                yourHealth = yourHealth - 4
        if Attack2 == 2:
            print(Opponent + " Used " + moves2[1])
            if crit2 == 1:
                yourHealth = yourHealth - 6
                print("A Critical Hit!")
            else:
                yourHealth = yourHealth - 12
        if Attack2 == 3:
            print(Opponent + " Used " + moves2[2])
            print("ERROR")
    else:
        print(Pokemon + "'s attack missed!")
# move end
# battle info
print(Pokemon + " vs " + Opponent)
time.sleep(1)
print("Go " + Pokemon)
time.sleep(1)
while yourHealth > 0 and opponentHealth > 0:
    moves()
    time.sleep(1)
    if opponentHealth <= 0:
        print(Opponent + " has " + "Fainted")
    else:
        print(Opponent + " has " + str(opponentHealth) + " Health")
        time.sleep(1)
    movesopponent()
    if yourHealth <= 0:
        print(Pokemon + " has " + "Fainted")
    else:
        print(Pokemon + " has " + str(opponentHealth) + " Health")
        time.sleep(1)
time.sleep(1)
if yourHealth <= 0:
    print("You Lose!")
if opponentHealth <= 0:
    print("You Win!")

