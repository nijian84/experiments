#Experiment 1, a Dice Roller app

from random import randint
from random import seed

#Ask user how many Dice
x = int(input("How many Dice do you wish to roll: "))
print("You wish to roll " + str(x) + " dice.")

#Declare valid Dice range
dieSides = {"d4" : 4, "d6" : 6, "d8" : 8, "d10" : 10, "d12" : 12, "d20" : 20, "d100" : 100}

#List Valid dice choice
for n in dieSides:
    print(n)

#Ask for input
y = int(input("Which dice would you like to roll? d"))
response = str(y)

#Check input for Valid dice choice
def validate(z):
    if z in iter(dieSides.values()):
        return 1
    else:
        return 0

#Run Validate function

#Calculate the sum of dice
def totalSum(count, sides):
    sum = 0
    seed(count + 1)
    for n in range(count):
        value = randint(0, sides)
        sum = sum + value
    return(sum)

if validate(y) == 1:
    result = totalSum(x, y)
    print("Your roll was: " + str(result))
else:
    print("Input invalid: " + response)