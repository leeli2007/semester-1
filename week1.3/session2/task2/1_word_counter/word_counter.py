# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210

file_name = input("Enter file name:")
count = 0
try:
    with open(file_name,'r') as inFile:
        for line in inFile:
            if len(line) > 1:
                temp = line.strip().split(" ")
                count += len(temp)

    print(f"{file_name} - {count}")
except FileNotFoundError:
    print("File not found")

