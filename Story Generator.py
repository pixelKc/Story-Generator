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
print("Choose your superpower")
print("Select 1-3")
print("Superpower 1: Seeing through walls")
print("Superpower 2: Talking to animals")
print("Superpower 3: Teleportation")
power = input()
if(power == "1"):
    power_1 = True
elif(power == "2"):
    power_2 = True
elif(power == "3"):
    power_3 = True
debugging("Superpower", power, debug)


# Potion Selector
potion_1 = False
potion_2 = False
potion_3 = False
print("A witch approaches you and offers 3 potions")
print("Select 1-3")
print("1. A Fire Resistance Potion that lasts for just 3 seconds, it will heal you and stop the fire from burning")
print("2. An Instant Healing potion that brings you up to full health")
print("3. An Invisibility Potion that will last just 3 minutes and allows you to sneak around enemies")
potion = input()
if(potion == "1"):
    potion_1 = True
elif(potion == "2"):
    potion_2 = True
elif(potion == "3"):
    potion_3 = True
# Displays Potion for debugging purposes (if debug mode is enabled)
debugging("potion", potion, debug)




print(f"{name}'s Adventure Begins")


# TODO: STEP #6: Write the main story
# Write a creative story (at least 3-4 sentences) that uses all three variables
# Make sure to use each variable at least once in your story
# Example: print(f"Once upon a time, {hero_name} discovered a mysterious {magical_weapon}...")
# Remember to use proper punctuation and make the story engaging!
if(power_1 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap).\n")
    print("You wake up in a mysterious prison cell with minimal security.\n")
    print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
    print("You remember that you purchased a fire resistance potion from a witch, so you slide through the bars, and just as you suspected, the creature runs over, and you battle.\n")
    print("He shoots fire at you, you use your potion, and then you defeat the monster.\n")
elif(power_1 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
    print("You remember that you purchased an instant healing potion from a witch, so you slide through the bars, and just as you suspected, the creature runs over, and you battle.\n")
    print("He shoots fire at you, you use your potion, and then you defeat the monster.\n")
elif(power_1 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You look around, and using your superpower to see through walls, you see a mysterious creature holding a flamethrower.\n")
    print("You remember that you purchased an invisibility potion from a witch, so you slide through the bars, and just as you suspected, the creature runs over, and you battle.\n")
    print("You use your potion, and then you walk over to him and defeat him undetected.\n")
elif(power_2 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you, you remember that you purchased a potion from a witch, you use it, you still can’t defeat the monster.\n")
    print("You notice a lion in another prison cell, you help him escape, and you work together to defeat the monster.\n")
elif(power_2 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you, you remember that you purchased a potion from a witch, you heal up, and you can’t defeat the monster.\n")
    print("You notice a lion in another prison cell, you help him escape, and you work together to defeat the monster.\n")
elif(power_2 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("You remember that you purchased a potion from a witch, you go invisible,\n")
    print("you notice a lion in another prison cell, you help him escape, and you work together to defeat the monster.\n")
elif(power_3 == True and potion_1 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you. You remember that you purchased a fire resistance potion from a witch,  you used your potion, you teleported behind the monster, and then you defeated the monster.\n")
elif(power_3 == True and potion_2 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. You remember that you purchased an instant healing potion from a witch, so you slide through the bars, a mysterious creature runs over, and you battle.\n")
    print("He shoots fire at you, you use your potion, you teleport behind the monster, and then you defeat the monster.\n")
elif(power_3 == True and potion_3 == True):
    print("You were peacefully eating breakfast when all of a sudden (Pow) (Zap)\n")
    print("You wake up in a mysterious prison cell with minimal security. so you slide through the bars, and a mysterious creature runs over, and you battle.\n")
    print("You remember you purchased an invisibility potion from a witch, you use your potion, and then you teleport over to him and defeat him undetected.\n")
# TODO: STEP #7: Add a story ending
# Print a creative ending for your story
# Example: print("\nThe End") or print("\nAnd they lived happily ever after!")
print("The End.")