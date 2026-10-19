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

        while True:
            aline = inFile.readline().lstrip()
            if len(aline) > 0 and aline[0] != "#":
                break
        widths_heights = aline.split()

        while True:
            aline = inFile.readline().lstrip()
            if len(aline) > 0 and aline[0] != "#":
                break
        max_gray_value = int(aline)

  
        height_count = 0
        gray_value_flag = True
        width,height = int(widths_heights[0]), int(widths_heights[1])

        for v in inFile:
            pixel = v.split()
            height_count += 1

            if int(width) != len(pixel):
                print("Invalid width")
                break

            for v in pixel:
                if int(v) < 0 or int(v) > max_gray_value:
                    gray_value_flag = False
                    break
            if not gray_value_flag:
                print("Invalid pixel values")
                break
             
        else:
            if height_count != height:
                print("Invalid height")
            else:
                print("Valid image")

except FileNotFoundError:
    print("File not found")