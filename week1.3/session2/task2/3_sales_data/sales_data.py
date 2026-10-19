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
widget = {}
sales_data = []
region = {}
total_sales = {}
region_widget={}

try:
    with open('sales.csv','r') as inFile:
        next(inFile)
        for v in inFile:
            words = v.strip().split(',')
            sales_data.append([words[0],words[1],int(words[2]),int(words[3]),words[4]])
 
    for words in sales_data:
        if words[2]> largest_sale:
            largest_sale = words[2]
            largest_sale_day = words[0]
        sum_sale_amount += words[2]

        widget[words[1]] = widget.get(words[1],0) + words[3]
        total_sales[words[1]] = total_sales.get(words[1],0) + words[2]
        region[words[-1]] = region.get(words[-1],0) + words[2]

        sale_weiget = region_widget.get(words[-1],{})
        sale_weiget[words[1]] = sale_weiget.get(words[1],0) + words[2]
        region_widget [words[-1]] = sale_weiget
        
    most_widget = max(widget.values())
    avg_sale_amount = sum_sale_amount / len(sales_data)
    print(f"Largest sale day is {largest_sale_day},average sale amount is {avg_sale_amount}, most sold widget is {max(widget.items(), key=lambda x: x[1])}")
    print(region)
    print(total_sales)
    print(region_widget)

except:
    print("Error")
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