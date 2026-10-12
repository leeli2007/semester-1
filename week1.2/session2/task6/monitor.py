# Week 1.2, Session 2: Task 6
temp = int(input())
pressure = int(input())
status = int(input())

if temp > 80:
    print("temperature is too high")
elif 50 <= temp <= 80:
    print("temperature is within safe limits")
else:
    print("temperature is low")

if pressure > 100:
    print("high pressure is detected")
elif 70 <= pressure <= 100:
    print(" pressure is stable.")
else:
    print("pressure is low")

if status == 1 and (temp > 80 or pressure > 100):
    print("machine is running in unsafe conditions and recommend shutting it down")
elif status == 0:
    print("it is stopped and no immediate action is needed.")
else:
    print("machine is running normally")