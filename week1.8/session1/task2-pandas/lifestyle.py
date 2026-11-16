import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print("Type of data:", type(data))

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total = len(data)
print("Total number of students:", total)

# Find the mean average GPA of the students
mean_GPA = data['GPA'].mean()
print("Mean GPA:", round(mean_GPA, 2))

# Find the standard deviation of how much sleep students get per day
sleep = data["Sleep_Hours_Per_Day"].std()
print("Standard deviation of sleep hours per day:", round(sleep, 2))

# Find the maximum amount of study hours per day
max_study_hour = data["Study_Hours_Per_Day"].max()
print("Maximum study hours per day:", max_study_hour)

# Sort the students by social hours per day ascending (lowest -> highest)
social = data.sort_values(by="Social_Hours_Per_Day",ascending=True)
print("Students by social hours per day ascending:",social)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = (
    data["Study_Hours_Per_Day"]
    + data["Extracurricular_Hours_Per_Day"]
    + data["Sleep_Hours_Per_Day"]
    + data["Social_Hours_Per_Day"]
    + data["Physical_Activity_Hours_Per_Day"]
)
print(data[["Total_hours"]].head(10))

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress = data[data["Stress_Level"] == "High"]
print(high_stress)

low_stress = data[data["Stress_Level"] == "Low"]
print(low_stress)

high_GPA = high_stress["GPA"].mean()
low_GPA = low_stress["GPA"].mean()
print(f"High stress GPA :{high_GPA:.3f}")
print(f"Low stress GPA :{low_GPA:.3f}")
