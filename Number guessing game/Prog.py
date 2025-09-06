import random

Random_Number = random.randint(1, 100)
print("Enter a number from 1 to 100: ")
while True:
    U = int(input("->  "))
    if U == Random_Number:
        print("You Win!")
        break
    elif U > Random_Number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again. \n")