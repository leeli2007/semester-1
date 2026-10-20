# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    '''
    Count the number of uppercase and lowercase letters in a string.
 
    Iterates over each character in the string and counts how many 
    are uppercase letters and how many are lowercase letters. 
 
    Args:
        string (str): The input string to analyze.
 
    Returns:
        tuple: A tuple of two integers: (uppercase_count, lowercase_count).
    '''

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X"))
print(mystery_func("[2, 3]"))
