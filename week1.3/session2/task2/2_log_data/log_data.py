# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file

# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20

file_name = input().strip()
with open(file_name,'r') as inFile:
    next(inFile)
    for v in inFile:
        temp = v.strip().split(',')
        if temp[-2] == "POST /login" and temp[-1] == "401":
            print(f"IP address {temp[2]} failed to login at {temp[1]} on {temp[0]}")

# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data