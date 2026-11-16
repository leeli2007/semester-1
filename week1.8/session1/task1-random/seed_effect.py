# See README.md for instructions on what to do this program

import random

#random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# When the same seed is used, the program generates
# the same sequence of random numbers every time.
# When the seed is changed, a different sequence is generated.
# When random.seed() is removed, the random numbers
# are usually different each time the program runs.