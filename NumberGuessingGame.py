import random

num = random.randint(1,9)
chances = 0
while(chances < 3):
    inp = int(input("Enter your choice"))
    if(num == inp):
        print("Wow! You have made the correct choice.")
        break
    elif(inp < num):
        print("Your guess was too low!")
    else:
        print("Your guess was too high!")
    chances = chances + 1