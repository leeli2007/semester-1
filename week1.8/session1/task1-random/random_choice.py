import random

# Read names from a file

with open("week1.8/session1/task1-random/names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
    nums = int(input("Enter many names you want:"))
    name = random.sample(names,k=nums)

# Display the chosen names, one per line
    [print(v) for v in name]
    v = [1,2,3,4,5,6,7,8,9]
    random.shuffle(v)
    [print(v3) for v3 in v]
