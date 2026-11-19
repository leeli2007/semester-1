import pandas
def makeDataFrame():
    student = pandas.DataFrame(
        {
            "name":["lxy","zj"],
            "sex":["male","female"],
            "age":[19,45],
            "tel":[44,86]
        }
    )
    print(student[["name","age"]])
    print(student["age"].max())
    print(student.describe())

def readDataFrame():
    life = pandas.read_csv("week1.8/session1/task2-pandas/lifestyle_data.csv")
    print(life.dtypes)

    sel_feilds = ["Extracurricular_Hours_Per_Day","Sleep_Hours_Per_Day"]
    data = life[sel_feilds]
    print(data)

    where=life["Study_Hours_Per_Day"]>6.0
    data2 = life[where]
    print(data2.shape)

    data3 = life.loc[where,sel_feilds]
    print(data3)
    
readDataFrame()