
# function implementation

def even_num(num):

    even_nums = [i for i in range(int(num)+1) if i % 2 == 0]

    return even_nums

print(f"Even integers between 0 and that value are{even_num(10)}") 