# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

largest_sale = 0
largest_sale_day = '0'
sum_sale_amount = 0
day_count = 0
widget = {"Widget_A":0,"Widget_B":0,"Widget_C":0,"Widget_D":0}

#additional tasks
Region = {"North":0,"South":0,"East":0,"West":0}
North = {"Widget_A":0,"Widget_B":0,"Widget_C":0,"Widget_D":0}
South = {"Widget_A":0,"Widget_B":0,"Widget_C":0,"Widget_D":0}
East = {"Widget_A":0,"Widget_B":0,"Widget_C":0,"Widget_D":0}
West = {"Widget_A":0,"Widget_B":0,"Widget_C":0,"Widget_D":0}


with open('sales.csv','r') as inFile:
    next(inFile)
    for v in inFile:
        temp = v.strip().split(',')
        if int(temp[2])> largest_sale:
            largest_sale = int(temp[2])
            largest_sale_day = temp[0]
        sum_sale_amount += int(temp[2])
        day_count += 1

        if temp[1] == "Widget A" :
            widget["Widget_A"] += int(temp[3])
        elif temp[1] == "Widget B" :
            widget["Widget_B"] += int(temp[3])
        elif temp[1] == "Widget C" :
            widget["Widget_C"] += int(temp[3])  
        elif temp[1] == "Widget D" :
            widget["Widget_D"] += int(temp[3])        

    most_widget = max(widget.values())
    avg_sale_amount = sum_sale_amount / day_count

    #additional tasks
    with open('sales.csv','r') as inFile:
        next(inFile)
        for v in inFile:
            temp = v.strip().split(',')

            if temp[4] == "North" :
                Region["North"] += int(temp[2])

                match temp[1]:
                    case "Widget A":
                        North["Widget_A"] += int(temp[3])
                    case "Widget B":
                        North["Widget_B"] += int(temp[3])
                    case "Widget C":
                        North["Widget_C"] += int(temp[3])
                    case "Widget D":
                        North["Widget_D"] += int(temp[3])                                           

            elif temp[4] == "South" :
                Region["South"] += int(temp[2])

                match temp[1]:
                    case "Widget A":
                        South["Widget_A"] += int(temp[3])
                    case "Widget B":
                        South["Widget_B"] += int(temp[3])
                    case "Widget C":
                        South["Widget_C"] += int(temp[3])
                    case "Widget D":
                        South["Widget_D"] += int(temp[3])  

            elif temp[4] == "East" :
                Region["East"] += int(temp[2])  
                match temp[1]:
                    case "Widget A":
                        East["Widget_A"] += int(temp[3])
                    case "Widget B":
                        East["Widget_B"] += int(temp[3])
                    case "Widget C":
                        East["Widget_C"] += int(temp[3])
                    case "Widget D":
                        East["Widget_D"] += int(temp[3]) 

            elif temp[4] == "West" :
                Region["West"] += int(temp[2])        
                match temp[1]:
                    case "Widget A":
                        West["Widget_A"] += int(temp[3])
                    case "Widget B":
                        West["Widget_B"] += int(temp[3])
                    case "Widget C":
                        West["Widget_C"] += int(temp[3])
                    case "Widget D":
                        West["Widget_D"] += int(temp[3]) 


print(f"Largest sale day is {largest_sale_day},average sale amount is {avg_sale_amount}, most sold widget is {max(widget.items(), key=lambda x: x[1])}")

#Additional tasks
print(f"North sales {Region["North"]},South sales {Region["South"]},East sales {Region["East"]},West sales {Region["West"]}")       
print(f"North most sold widget is {max(North.items(), key=lambda x: x[1])}")
print(f"South most sold widget is {max(South.items(), key=lambda x: x[1])}")
print(f"East most sold widget is {max(East.items(), key=lambda x: x[1])}")
print(f"West most sold widget is {max(West.items(), key=lambda x: x[1])}")
print(f"Widget A total sales {widget["Widget_A"]}, Widget B total sales {widget["Widget_B"]}, Widget C total sales {widget["Widget_C"]}, Widget D total sales {widget["Widget_D"]}")       


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget

# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows