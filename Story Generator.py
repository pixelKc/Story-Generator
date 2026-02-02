import sys

# Variable to determine if the software is in debug mode
debug = False

# Check if the argument "debug" is passed when running the software
try: 
    if(sys.argv[1] == "debug"):
        debug = True
except:
    print(end="")
# Debug Mode (If code above is true)
def debugging(Experiment, Var, Debug):
    if(Debug == True):
        if(Experiment == "name"):
            print("Debug Message: Name", Var)
        elif(Experiment == "potion"):
            if(Var == "1"):
                print("Debug Message: Potion 1 selected")
            elif(Var == "2"):
                print("Debug Message: Potion 2 selected")
            elif(Var == "3"):
                print("Debug Message: Potion 3 selected")
        elif(Experiment == "Superpower"):
            if(Var == "1"):
                print("Debug Message: Superpower 1 selected")
            if(Var == "2"):
                print("Debug Message: Superpower 2 selected")
            if(Var == "3"):
                print("Debug Message: Superpower 3 selected")

print("Story Genarator... but you're the hero")

# Gets the players name
name = input("What is your name?\n")
# Displays name for debugging purposes (if debug mode is enabled)
debugging("name", name, debug)

# Superpower Selector
power_1 = False
power_2 = False
power_3 = False
while True:
    print("Choose your superpower")
    print("Select 1-3")
    print("Superpower 1: Seeing through walls")
    print("Superpower 2: Talking to animals")
    print("Superpower 3: Teleportation")
    power = input()
    if(power == "1"):
        power_1 = True
        break
    elif(power == "2"):
        power_2 = True
        break
    elif(power == "3"):
        power_3 = True
        break
    else:
        print("That is out of the range, please select a number between 1-3")
debugging("Superpower", power, debug)


# Potion Selector
potion_1 = False
potion_2 = False
potion_3 = False
while True:
    print("A witch approaches you and offers 3 potions")
    print("Select 1-3")
    print("1. A Fire Resistance Potion that lasts for just 3 seconds, it will heal you and stop the fire from burning")
    print("2. An Instant Healing potion that brings you up to full health")
    print("3. An Invisibility Potion that will last just 3 minutes and allows you to sneak around enemies")
    potion = input()
    if(potion == "1"):
        potion_1 = True
        break
    elif(potion == "2"):
        potion_2 = True
        break
    elif(potion == "3"):
        potion_3 = True
        break
    else:
        print("That is out of the range, please select a number between 1-3")
debugging("potion", potion, debug)

print(f"{name}'s Adventure Begins")
if(power_1 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap).\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    while True:
        print("Seeing through walls (1)")
        print("Fire Resistance potion (2)")
        Power = input("Select a power to use (1 or 2)")
        if(Power == "1"):
            print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.")
            print("you slide through the bars, and just as you suspected, the creature runs over, and you battle.")
            print("He shoots fire at you")
            while True:
                print("Seeing through walls (1)")
                print("Fire Resistance potion (2)")
                Power = input("Select a power to use (1 or 2)")
                if(Power == "1"):
                    print("bruh")
                    sys.exit(0)
                elif(Power == "2"):
                    print("you use your fire resistance potion, and then you defeat the monster.")
                    break
                else:
                    print("That is out of the range, please select a number between 1-2")
        elif(Power == "2"):
            print("You jump out of the cell, and a mysterious creature jumps out, you battle")
            print("He shoots fire at you, thank goodness you used the fire resistance potion")
            print("You defeat the creature")
            break
        else:
            print("That is out of the range, please select a number between 1-2")
elif(power_1 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    while True:
        print("Seeing through walls (1)\n")
        print("Instant Healing potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
            print("so, you slide through the bars and just as you suspected the creature runs over and you battle.\n")
            print("He shoots fire at you\n")
            while True:
                print("Seeing through walls (1)\n")
                print("Instant Healing Potion (2)\n")
                Power = input("Select a power to use (1 or 2)\n")
                if(Power == "1"):
                    print("bruh")
                    sys.exit()
                elif(Power == "2"):
                    print("you use your potion, and then you defeat the monster.\n")
                    break
                else:
                    print("That is out of the range, please select a number between 1-2")
        elif(Power == "2"):
            print("YOU WERE ALREADY AT FULL HEALTH... you're trapped... GAME OVER")
            sys.exit(0)
elif(power_1 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    print("Seeing through walls (1)\n")
    print("invisibility potion (2)\n")
    Power = input("Select a power to use (1 or 2)")
    if(Power == "1"):
        print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
        print("you slide through the bars, and just as you suspected, the creature runs over, and you battle.\n")
        print("Seeing through walls (1)\n")
        print("Invisibility Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("bruh")
            sys.exit(0)
        elif(Power == "2"):
            print("You use your potion and the creature looses you and you defeat him\n")
        else:
            print("That is out of the range, please select a number between 1-2")
    elif(Power == "2"):
        print("You use your potion and slide through the bars.\n")
        print("You see a mysterious creature, so you sneak up and defeat himd")
    else:
        print("That is out of the range, please select a number between 1-2")
elif(power_2 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you.\n")
    print("Talking to animals (1)\n")
    print("Fire Resistance Potion (2)\n")
    Power = input("Select a power to use (1 or 2)\n")
    if(Power == "1"):
        print("You dodge the fire attack and notice a lion in another prison cell.\n")
        print("you help him escape")
        print("you see a mysterious creature, you defeat the creature together")
    elif(Power == "2"):
        print("Your not on fire anymore, but you still can't defeat the creature")
        print("You notice a lion in another prison cell.\n")
        print("Talking to animals (1)\n")
        print("Fire Resistance Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("you help him escape, and you work together to defeat the monster")
        elif(Power == "2"):
            print("Well... about that... you already used that one... GAME OVER")
            sys.exit(0)
        else:
            print("That is out of the range, please select a number between 1-2")
    else:
        print("That is out of the range, please select a number between 1-2")
elif(power_2 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you.\n")
    print("Talking to animals (1)\n")
    print("Instant Healing Potion (2)\n")
    Power = input("Select a power to use (1 or 2)\n")
    if(power == "1"):
        print("YOU'RE STILL ON FI- oooohhh game over :(")
        sys.exit(0)
    elif(power == "2"):
        print("You heal up but you still can't defeat the creature")
        print("You notice a lion in another prison cell.\n")
        print("Talking to animals (1)\n")
        print("Instant Healing Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("You help the lion escape and you work together to defeat the monster.")
        elif(Power == "2"):
            print("Well... about that... you already used that one... GAME OVER")
            sys.exit(0)
        else:
            print("That is out of the range, please select a number between 1-2")
    else:
        print("That is out of the range, please select a number between 1-2")

elif(power_2 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over.\n")
    print("Talking to animals (1)")
    print("Invisibility Potion (2)")
    Power = input("Select a power to use (1 or 2)")
    if(Power == "1"):
        print("How is that going to help you? GAME OVER")
        sys.exit(0)
    elif(Power == "2"):
        print("Before he sees you, you go invisible")
        print("You notice a lion in another prison cell")
        print("Talking to animals (1)\n")
        print("Invisibility Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("you free the lion and work together to defeat the mysterious creature")
        elif(Power == "2"):
            print("You already used that one. oh no, your invisibility ran out. GAME OVER")
            sys.exit(0)
        else:
            print("That is out of the range, please select a number between 1-2")
    else:
        print("That is out of the range, please select a number between 1-2")
elif(power_3 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you")
    print("Teleportation (1)\n")
    print("Fire Resistance Potion (2)\n")
    Power = input("Select a power to use (1 or 2)\n")
    if(Power == "1"):
            print("You teleport behind the monster and you're about to defeat him but WAAAAIT... you're... still on fire GAME OVER :(")
    elif(Power == "2"):
        print("You aren't on fire anymore but you still can't defeat him...")
        print("Teleportation (1)\n")
        print("Fire Resistance Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("You teleport behind the monster and defeat him")
        elif(Power == "2"):
            print("You already used that one. oh no, your invisibility ran out. GAME OVER")
            sys.exit(0)
        else:
            print("That is out of the range, please select a number between 1-2")
    else:
        print("That is out of the range, please select a number between 1-2")
elif(power_3 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security")
    print("You slide through the bars and a mysterious creature with a flamethrower runs over, and he shoots fire at you.\n")
    print("Teleportation (1)\n")
    print("Instant Healing Potion (2)\n")
    Power = input("Select a power to use (1 or 2)\n")
    if(Power == "2"):
        print("You're no longer on fire but you still can't beat the monster")
        print("Teleportation (1)\n")
        print("Instant Healing Potion (2)\n")
        Power = input("Select a power to use (1 or 2)\n")
        if(Power == "1"):
            print("You teleport behind the monster and defeat him.")
        elif(Power == "2"):
            print("You already used that one. GAME OVER :(")
            sys.exit(0)
        else:
            print("That is out of the range, please select a number between 1-2")
    elif(Power == "1"):
        print("You teleport behind the monster and you're about to defeat him but WAAAAIT... you're... still on fire GAME OVER :(")
        sys.exit(0)
    else:
        print("That is out of the range, please select a number between 1-2")
elif(power_3 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. so you slide through the bars, and a mysterious creature runs over, and you battle\n")
    print("Teleportation (1)\n")
    print("Invisibility (2)\n")
    Power = input("Select a power to use (1 or 2)\n")
    if(Power == "1"):
            print("You teleport behind the monster and you defeat him")
    elif(Power == "2"):
        print("You use your invisibility potion and you are able to defeat him")
    else:
        print("That is out of the range, please select a number between 1-2")
print("The End.")
