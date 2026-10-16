# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

fileName = input()
fileName = "../images/" + fileName

try:
    with open(fileName,'r') as inFile:
        next(inFile)
        line = inFile.readline().split("#")[0].strip()
        while line == "":
            line = inFile.readline().split("#")[0].strip()
        widths_heights = line.split()

        line = inFile.readline().split("#")[0].strip()
        while line == "":
            line = inFile.readline().split("#")[0].strip()
        max_gray_value = int(line)

        width_flag = True
        height_flag = 0
        gray_value_flag = True

        for v in inFile:
            temp = v.split()
            height_flag += 1

            if int(widths_heights[0]) != len(temp):
                width_flag = False

            for v in temp:
                if int(v) < 0 or int(v) > max_gray_value:
                    gray_value_flag = False

        if width_flag == True and height_flag == int(widths_heights[1]) and gray_value_flag == True:
            print("Valid image")
        else:
            if width_flag == False:
                print("Invalid width")
            if height_flag != int(widths_heights[1]):
                print("Invalid height")
            if gray_value_flag != True:
                print("Invalid pixel values")

except FileNotFoundError:
    print("File not found")