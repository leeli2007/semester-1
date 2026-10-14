# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

import csv

file_name = input().strip()

# open the file
with open(file_name,'r') as infile: 
   with open(file_name+"_out.csv",'w') as outfile:
# read in the data, and for each student calculate their average grade and classification

      res = ""
      next(infile)
      for line in infile:
         result = line.strip().split(',')
         cleaned_result = [int(item) for item in result if len(item) != 0 and item.isdigit()] 
         print(cleaned_result)
         avg = sum(cleaned_result) / len(cleaned_result)
        
         grade = -1
         if avg >= 70:
            grade = '1'
         elif avg >= 60:
            grade = "2:1"
         elif avg >= 50:
            grade = "2:2"
         elif avg >= 40:
            grade = "3"
         else:
            grade = 'F'
         print(str(format(avg,'.2f')),sum,grade)

         res = result[0]+','+ str(format(avg,'.2f')) + ',' +grade+"\n"
         outfile.write(res)

      


# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder