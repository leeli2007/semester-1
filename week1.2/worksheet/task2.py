# Worksheet 1.2: Task 2 Solution
import sys 

try:
    ip = input("Input a sequence of float values: ") 
    words = ip.split(",")
    nums = []
    for s in words:
        nums.append(float(s))

except ValueError:    
    sys.exit("Error: no numbers provided") 

sorted_nums = sorted(nums)
mean = sum(sorted_nums) / len(sorted_nums)
mid = len(sorted_nums) // 2
if (len(sorted_nums) % 2 == 1):
    median = sorted_nums[mid]
else:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    
print(f"Minimum = {sorted_nums[0]}")
print(f"Maximum = {sorted_nums[-1]}")
print(f"Mean = {mean}")
print(f"Median = {median}")
