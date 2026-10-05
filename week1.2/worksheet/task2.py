# Worksheet 1.2: Task 2 Solution
import sys 

try:
    ip = input("Input a sequence of float values: ") 
    nums = [float(s) for s in ip.split(",")] 
except ValueError:    
    sys.exit("Error: no numbers provided") 
 
minimum = min(nums) 
maximum = max(nums) 
mean = sum(nums) / len(nums) 
 
sorted_nums = sorted(nums) 
length = len(sorted_nums) 
mid = length // 2 
if length % 2 == 1: 
    median = sorted_nums[mid] 
else: 
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 
 
print(f"Minimum = {minimum}") 
print(f"Maximum = {maximum}") 
print(f"Mean = {mean}") 
print(f"Median = {median}") 