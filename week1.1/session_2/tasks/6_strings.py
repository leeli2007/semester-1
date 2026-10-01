# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
#print original string again
print(f"Modified String 1: {user_string.lower()}")
#change all characters to lowercase
print(f"Modified String 2: {user_string.upper()}")
#change all characters to uppercase
print(f"Modified String 3: {user_string.strip()}")
#remove whitespace from the beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}")
#replace all 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}")
#make the first character of the string uppercase       
print(f"Modified String 6: {user_string[::-1]}")
#reverse the string
print(f"Modified String 7: {user_string.title()}")
#make the first character of each word in the string uppercase
print(f"Modified String 8: {len(user_string)}")
#return the length of the string
print(f"Modified String 9: {user_string.find('a')}")
#find the first occurrence of 'a'
print(f"Modified String 10: {user_string.count('a')}")
#count the number of occurrences of 'a'
print(f"Modified String 11: {user_string.startswith('Hello')}")
#check if the string starts with 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}")
#check if the string ends with '!'
print(f"Modified String 13: {user_string.isalnum()}")
#check if the string is alphanumeric
print(f"Modified String 14: {user_string.isalpha()}")
#check if the string is alphabetic
print(f"Modified String 15: {user_string.isdigit()}")
#check if the string is a digit


######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!