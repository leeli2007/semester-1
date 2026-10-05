# Worksheet 1.2: Task 1 Solution
import sys
grade = input()

if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade)

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if 0 <= grade <= 39: 
    result = "Fail" 
elif 40 <= grade <= 69: 
    result = "Pass" 
else: 
    result = "Distinction" 

print(f"{grade} is a {result}") 