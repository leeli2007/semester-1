# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"

fileName = input()
fileName = "../images/" + fileName

try:
    with open(fileName, 'r') as inFile:
        with open("Inverted_Image.pgm", 'w') as outFile:
            title = inFile.readline().strip() + "\n"
            outFile.write(title)
            dimensions = inFile.readline().strip() + "\n"
            outFile.write(dimensions)
            maximum_gray_value = inFile.readline().strip()
            outFile.write(maximum_gray_value + "\n")

            for line in inFile:
                value = line.split()
                for index in range(len(value)):
                    value[index] = str(int(maximum_gray_value) - int(value[index]))

                line = " ".join(str(v) for v in value)
                outFile.write(line + "\n")

except FileNotFoundError:
    print("File not found")