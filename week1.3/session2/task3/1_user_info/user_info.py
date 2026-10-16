# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'

with open('user_info.txt' , 'w') as outFile:
    while True:
        print("Please enter your name, age, and favourite colour,quit to exit")
        name = input().strip()
        age = input().strip()
        favourite_color = input().strip()

        if name == "quit" or age == "quit" or favourite_color == "quit":
            break

        temp = name + ' ' + age + ' ' + favourite_color + "\n"
        outFile.write(temp) 
with open('user_info.txt' , 'w') as outFile:
    while True:
        print("Please enter your name, age, and favourite colour,quit to exit")
        name = input().strip()
        age = input().strip()
        favourite_color = input().strip()

        if name == "quit" or age == "quit" or favourite_color == "quit":
            break

        temp = name + ' ' + age + ' ' + favourite_color + "\n"
        outFile.write(temp) 