# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'

try:
    with open('user_info.txt' , 'a') as outFile:
        while True:
            print("Please enter your name, age, and favourite colour,seperate by space enter quit to exit")
            information = input().strip().split()
            if len(information)==0 or information[0] == "quit" :
                break

            temp = information[0] + ' ' + information[1] + ' ' + information[2] + "\n"
            outFile.write(temp) 
except:
    print("Error")