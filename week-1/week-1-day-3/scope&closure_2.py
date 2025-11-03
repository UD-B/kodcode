#1
x = 10
def show():
    global x
    x = 5
    # print("Inside:", x)
    return x
show()
# print("Outside:", x)

# the function 'show' before adding global was aware
# only of the inner variable x while the outer doesen't
# change from inside functions

#2
count = 0
def add():
    global count
    count += 1
    # print(count)
add()

# it failed because the inner function has no initialized
# variable 'count' to increment

#3
msg = "Hi"
def outer():
    msg = "Hello"
    def inner():
        # print(msg)
        pass
    inner()
outer()

# msg comes from the enclosing function and sice it returs
# thr inner it is aware of "Hello"

#4
def counter():
    num = 0
    def add_one():
        nonlocal num
        num += 1
        # print(num)
    add_one()
counter()

# because there is no global variable caled num

#5
name = "Tom"
def greet():
    name = "Ben"
    print("Hi", name)
    return name
name = greet()
# print("Bye", name)