# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

try:
    with open("student_data.csv",'r') as inFile:
        with open("report.txt",'w') as outFile:
            next(inFile)
            for v in inFile:
                temp = v.split(',')
                avg = format((int(temp[2])+int(temp[3])+int(temp[4])) / 3,'.2f')
                str = "ID "+temp[0]+" name "+temp[1]+" average score is "+avg+"\n"
                outFile.write(str)
except:
    print("Error")            
