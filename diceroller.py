# A new experiment to write a simple Dice Roller program

#Import randint from Random functions
from random import randint

#Define the main application
#def main():

#Declare valid Dice range
dieSides = {"d4" : 4, "d6" : 6, "d8" : 8, "d10" : 10, "d12" : 12, "d20" : 20, "d100" : 100}

def userInput():
    #Ask user how many Dice
    x = int(input("How many Dice do you wish to roll:  ? (enter 0 to quit)"))
    if x > 0:
        print("You wish to roll " + str(x) + " dice.")
    else:
        print("Quitting...")
    
    #List Valid dice choice
    for n in dieSides:
        print(n)

    #Ask for input
    y = int(input("Which dice would you like to roll? d"))
    response = str(y)
    
    #Returns input Values
    return (x, y, response)

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
        value = randint(0, sides)
        sum = sum + value
    return(sum)

#Invoke userInput function and map responses to Variables

(a,b,c) = userInput()



#Run Validate function



if validate(b) == 1:
    result = totalSum(a, b)
    print("Your roll was: " + str(result))
else:
    print("Input invalid: " + c)


#if __name__ == '__main__': main()