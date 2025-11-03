"""
this function takes a number as an argument and returns
a matrix with the number of rows and linesas the argument.
the values of the elements in each line are the increments
of the number of the line.
"""
def mat_size(size: int):
    for i in range(1, size + 1):
        print(" ")
        for j in range(1, size + 1):
            print(i * j, end = " ")
    print('')
    return ""
mat_size(3)

def pyramid(height: int):
    for i in range(1, height + 1):
        print(" ")
        for j in range(1, i + 1):
            print(j, end = " ")
    print('')
    return ""
pyramid(4)

def star_pyramid(height: int):
    for i in range(1, height + 1):
        print("")
        print(i * "*")
    return ""
star_pyramid(5)

def if_else(size: int):
    for i in range(1, size + 1):
        print(" ")
        for j in range(1, size + 1):
            if i == j:
                print(1, end = " ")
            else:
                print(0, end = " ")
    print('')
    return ""
if_else(4)

def upside_down(height: int):
    for i in range(height, 0, -1):
        print(' ')
        print(i * "*")
    print('')
    return ""
upside_down(4)

def sum_elements(size: int):
    sum = 0
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            sum += i * j
    print(f'"the sum of such matrix is {sum}"')
    return ""
sum_elements(3)






print('')
print('')