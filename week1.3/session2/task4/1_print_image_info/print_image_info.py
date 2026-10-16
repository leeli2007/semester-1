# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)

fileName = input()
fileName = "../images/" + fileName

try:
    with open(fileName,'r') as inFile:
        next(inFile)
        temp = inFile.readline().strip().split(" ")
        dimension = int(temp[0])*int(temp[1])
        print(f"Image dimension is {dimension}")
        max_gray_value = inFile.readline()
        print(f"Max gray value is {max_gray_value}")
      

except FileNotFoundError:
    print("File not found")
