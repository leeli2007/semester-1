
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) # count how many numbers stored in variable
    for value in lst_value: 
        sum = sum + value  # calculate total value of numbers
    return sum/num_of_value  # calculate average value

print(func_1([1,2,3,4,5]))