# A new experiment to write a simple Dice Roller program

#Import randint from Random functions
from random import randint

#Define the main application
#def main():

#Declare valid Dice range
dieSides = {"d4" : 4, "d6" : 6, "d8" : 8, "d10" : 10, "d12" : 12, "d20" : 20, "d100" : 100}

def userInput():
    #Ask user how many Dice
    while True:
        try:
            x = int(input("How many Dice do you wish to roll? (enter 0 to quit) "))
        except ValueError:
            print("Please enter in a valid number.")
            continue
        else:            
            if x > 0:
                print("You wish to roll " + str(x) + " dice.")
                for n in dieSides:
                    print(n)
                break
            else:
                print("Quitting...")
                return (x, 0)

    #Ask for input
    while True:
        try:
            y = int(input("Which dice would you like to roll? d"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break

    #Validate input is valid dice, until valid
    while validate(int(y)) == 0:
        print("Please enter in a valid choice, from the list:")
        for n in dieSides:
            print(n)
        y = int(input("Which dice would you like to roll? d"))

    #Returns input Values
    return (x, y)

#Check input for Valid dice choice
def validate(z):
    if z in iter(dieSides.values()):
        return 1
    else:
        return 0

#Calculate the sum of dice
def totalSum(count, sides):
    sum = 0
    for n in range(count):
        value = randint(1, sides)
        sum = sum + value
    return(sum)

#Main function
def main():
    j = 1
    while j >= 1:
        (a,b) = userInput()
        if a >= 1:
            result = totalSum(a, b)
            print("Your roll was: " + str(result))                
        if a == 0:
            print("Thanks for using DiceRoller.")
            break

#Invoke Main function
if __name__ == "__main__":
  main()