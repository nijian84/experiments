# A new experiment to write a simple Dice Roller program

#Import randint from Random functions
from random import randint

#Declare valid Dice range
VALID_DICE = [4, 6, 8, 10, 12, 20, 100]

#Input for number of rolls
def user_input():
    """
    user_input: Prompts the user for input for number of rolls
    Arguments: None
    Returns: diceCount: int
    """
    while True:
        #Prompt user input
        try:
            diceCount = int(input("How many Dice do you wish to roll? (enter 0 to quit) "))
        #Validates int
        except ValueError:
            print("Please enter in a valid number.")
            continue
        #Declare count or quit application
        else:
            if diceCount > 0:
                print(f"You wish to roll {diceCount} dice.")
                for n in VALID_DICE:
                    print(f"d{n}")
                return diceCount
            else:
                print("Quitting...")
                diceCount = 0
                return diceCount

#Input for which dice to use
def dice_input():
    """
    user_input: Prompts the user for input for type of dice
    Arguments: None
    Returns: diceChoice: int
    """
    while True:
        #Prompt for dice type choice
        try:
            diceChoice = int(input("Which dice would you like to roll? d"))
        #Validates int
        except ValueError:
            print("Please enter a valid number.")
            continue
        #Displays choice, or prompts for Valid choice
        else:
            if valid_dice_checker(diceChoice):
                print(f"You chose: d{diceChoice}")
                return diceChoice
            else:
                print("Please enter in a valid choice, from the list.")
                for n in VALID_DICE:
                    print(f"d{n}")

#Validate dice sides input
def valid_dice_checker(choice):
    """
    Simple validation of dice choice
    Args: choice from dice_input
    Returns: boolean
    """
    return choice in VALID_DICE

#Calculate Sum of # of dice and sides of dice
def total_sum(count, sides):
    """
    Simple math
    Args: count from user_input and sides from dice_input
    Returns: sum: int
    """
    sum = 0
    #Takes number of rolls and randint in range of the dice type
    for _ in range(count):
        value = randint(1, sides)
        sum = sum + value
    return(sum)

def main():
    """
    Main function, prompts user input, quits if 0, or displays sum of rolls, and repeats until quit
    Args: None
    Returns: None
    """
    j = 1
    while j >= 1:
        #Prompt rolls input
        diceCount = user_input()
        #If rolls is 0, then quit
        if diceCount == 0:
            print("Thanks for using DiceRoller.")
            break
        #Prompts type of dice
        diceChoice = dice_input()
        #Passes in args and calculates sum
        if diceCount >= 1:
            result = total_sum(diceCount, diceChoice)
            print(f"Your roll was: {result}")

#Invoke Main function
if __name__ == "__main__":
  main()
