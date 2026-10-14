"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Xinyuan Li
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())+1  # read an integer number of steps (>0)

state = "red"

while maxtime > 0:
    for k,v in states.items():
        if maxtime >= v:
            for i in range(0,v):
                print(f"Time {systime:03} State {k}")
                systime += 1 
            maxtime -= v
        else:
            for i in range(0,maxtime):
                print(f"Time {systime:03} State {k}")
                systime += 1
            maxtime = 0
            break



# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14