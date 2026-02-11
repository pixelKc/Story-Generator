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

def get_player_info():#{
    name = input("What is your name?\n")
    # Displays name for debugging purposes (if debug mode is enabled)
    debugging("name", name, debug)
    return name

def intro(name, power, potion):
    print(f"Our hero {name} has the power of {power} and the {potion} potion\n")
    print(f"{name} begins their adventure")

def get_power_name(power): # Gosh this is so stupid
    if(power == "1"):
        power_name = "Seeing through walls"
    elif(power == "2"):
        power_name = "Talking to animals"
    elif(power == "3"):
        power_name = "Teleportation"
    return power_name

def get_potion_name(potion):
    if(potion == "1"):
        potion_name = "Fire resistance potion"
    elif(potion == "2"):
        potion_name = "Instant healing potion"
    elif(potion == "3"):
        potion_name = "Invisibility potion"
    return potion_name



"""
The following code is an example of "Do as I say not as I do"
Let me list out the problems
1. I used if statements for some reason.
2. I didn't convert the user input into an integer.
3. I made 3 boolean variables (WHAT)

WHAT WAS I THINKING

"""
def get_power():
    power_1 = False
    power_2 = False
    power_3 = False
    while True:#{
        print("Choose your superpower")
        print("Select 1-3")
        print("Superpower 1: Seeing through walls")
        print("Superpower 2: Talking to animals")
        print("Superpower 3: Teleportation")
        power = input()
        if(power == "1"):#{
            power_1 = True
            break
        #}
        elif(power == "2"):#{
            power_2 = True
            break
        #}
        elif(power == "3"):#{
            power_3 = True
            break
        #}
        else:#{
            print("That is out of the range, please select a number between 1-3")
        #}
        debugging("Superpower", power, debug)
    #} I like brackets (GAH I'M USED TO PHP)
    return power, power_1, power_2, power_3


# Potion Selector
def get_potion():
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
    return potion, potion_1, potion_2, potion_3


def story_1_1(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap).\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    while True:
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.")
            print("you slide through the bars, and just as you suspected, the creature runs over, and you battle.")
            print("He shoots fire at you")
            while True:
                Power = display_choice(power_name, potion_name)
                if(Power == "1"):
                    print("bruh")
                    sys.exit(0)
                elif(Power == "2"):
                    print("you use your fire resistance potion, and then you defeat the monster.")
                    break
        elif(Power == "2"):
            print("You jump out of the cell, and a mysterious creature jumps out, you battle")
            print("He shoots fire at you, thank goodness you used the fire resistance potion")
            print("You defeat the creature")
            break
def story_1_2(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    while True:
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
            print("so, you slide through the bars and just as you suspected the creature runs over and you battle.\n")
            print("He shoots fire at you\n")
            while True:
                Power = display_choice(power_name, potion_name)
                if(Power == "1"):
                    print("bruh")
                    sys.exit()
                elif(Power == "2"):
                    print("you use your potion, and then you defeat the monster.\n")
                    break
        elif(Power == "2"):
            print("YOU WERE ALREADY AT FULL HEALTH... you're trapped... GAME OVER")
            sys.exit(0)
def story_1_3(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    Power = display_choice(power_name, potion_name)
    if(Power == "1"):
        print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
        print("you slide through the bars, and just as you suspected, the creature runs over, and you battle.\n")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("bruh")
            sys.exit(0)
        elif(Power == "2"):
            print("You use your potion and the creature looses you and you defeat him\n")
    elif(Power == "2"):
        print("You use your potion and slide through the bars.\n")
        print("You see a mysterious creature, so you sneak up and defeat himd")
def story_2_1(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you.\n")
    Power = display_choice(power_name, potion_name)
    if(Power == "1"):
        print("You dodge the fire attack and notice a lion in another prison cell.\n")
        print("you help him escape")
        print("you see a mysterious creature, you defeat the creature together")
    elif(Power == "2"):
        print("Your not on fire anymore, but you still can't defeat the creature")
        print("You notice a lion in another prison cell.\n")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("you help him escape, and you work together to defeat the monster")
        elif(Power == "2"):
            print("Well... about that... you already used that one... GAME OVER")
            sys.exit(0)
def story_2_2(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you.\n")
    power = display_choice(power_name, potion_name)
    if(power == "1"):
        print("YOU'RE STILL ON FI- oooohhh game over :(")
        sys.exit(0)
    elif(power == "2"):
        print("You heal up but you still can't defeat the creature")
        print("You notice a lion in another prison cell.\n")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("You help the lion escape and you work together to defeat the monster.")
        elif(Power == "2"):
            print("Well... about that... you already used that one... GAME OVER")
            sys.exit(0)
def story_2_3(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over.\n")
    Power = display_choice(power_name, potion_name)
    if(Power == "1"):
        print("How is that going to help you? GAME OVER")
        sys.exit(0)
    elif(Power == "2"):
        print("Before he sees you, you go invisible")
        print("You notice a lion in another prison cell")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("you free the lion and work together to defeat the mysterious creature")
        elif(Power == "2"):
            print("You already used that one. oh no, your invisibility ran out. GAME OVER")
            sys.exit(0)
def story_3_1(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you")
    Power = display_choice(power_name, potion_name)
    if(Power == "1"):
            print("You teleport behind the monster and you're about to defeat him but WAAAAIT... you're... still on fire GAME OVER :(")
    elif(Power == "2"):
        print("You aren't on fire anymore but you still can't defeat him...")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("You teleport behind the monster and defeat him")
        elif(Power == "2"):
            print("You already used that one. oh no, your invisibility ran out. GAME OVER")
            sys.exit(0)
def story_3_2(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security")
    print("You slide through the bars and a mysterious creature with a flamethrower runs over, and he shoots fire at you.\n")
    Power = display_choice(power_name, potion_name)
    if(Power == "2"):
        print("You're no longer on fire but you still can't beat the monster")
        Power = display_choice(power_name, potion_name)
        if(Power == "1"):
            print("You teleport behind the monster and defeat him.")
        elif(Power == "2"):
            print("You already used that one. GAME OVER :(")
            sys.exit(0)
    elif(Power == "1"):
        print("You teleport behind the monster and you're about to defeat him but WAAAAIT... you're... still on fire GAME OVER :(")
        sys.exit(0)
def story_3_3(power_name, potion_name):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. so you slide through the bars, and a mysterious creature runs over, and you battle\n")
    Power = display_choice(power_name, potion_name)
    if(Power == "1"):
        print("You teleport behind the monster and you defeat him")
    elif(Power == "2"):
        print("You use your invisibility potion and you are able to defeat him")
# Again, do as I say, not as I do
def display_choice(power_name, potion_name):
    while True:
        print(f"{power_name} (1)\n")
        print(f"{potion_name} (2)\n")
        Power = input("Select a power to use")
        if Power in ["1", "2"]:
            return Power
        else:
            print("That is out of the range, please select a number between 1-2")
        



def main():
    name = get_player_info()
    power, power_1, power_2, power_3 = get_power()
    potion, potion_1, potion_2, potion_3 = get_potion()
    power_name = get_power_name(power)
    potion_name = get_potion_name(potion)
    intro(name, power_name, potion_name)
    if(power_1 == True and potion_1 == True):
        story_1_1(power_name, potion_name)
    elif(power_1 == True and potion_2 == True):
        story_1_2(power_name, potion_name)
    elif(power_1 == True and potion_3 == True):
        story_1_3(power_name, potion_name)
    elif(power_2 == True and potion_1 == True):
        story_2_1(power_name, potion_name)
    elif(power_2 == True and potion_2 == True):
        story_2_2(power_name, potion_name)
    elif(power_2 == True and potion_3 == True):
        story_2_3(power_name, potion_name)
    elif(power_3 == True and potion_1 == True):
        story_3_1(power_name, potion_name)
    elif(power_3 == True and potion_2 == True):
        story_3_2(power_name, potion_name)
    elif(power_3 == True and potion_3 == True):
        story_3_3(power_name, potion_name)
    print("The End.")

main()
