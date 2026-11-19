import random

# Get user to input how many random numbers they want
nums = int(input("Input numbers you want:"))

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
with open("week1.8/session1/task1-random/random.txt",'w') as outFile:
    for index in range(0,nums):
        randint = random.randint(0,100)
        outFile.write(str(randint)+"\n")
