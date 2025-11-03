#1
def say_hi_hi(func):
    def wrap(name):
        print("hi", name)
        func()
        print("bye")
    return wrap

@say_hi_hi
def ask():
    print("how are you")

# ask("UD")

#2
def mesure_time(func):
    def wrap():
        import time
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrap

@mesure_time
def sky():
    print("the sky is beautiful today")

# sky()

#3
def print_args(func):
    def wrap(age):
        func(age)
        print("this is the argument that was passed to the function", age)
    return wrap

@print_args
def your_age(age):
    print(f"you are {age} years old")

# your_age("24")

#4
def convert_to_uppercase(func):
    def wrap(*args):
        l = []
        for i in args:
            if type(i) == str:
                l.append(i.upper())
        return l
        func()
    return wrap

@convert_to_uppercase
def my_name_and_age(*args):
    pass

# print(my_name_and_age("hi", "bye 24", 24))

#5

def call_count(func):
    count = 0
    def wrap():
        nonlocal count
        count += 1
        func()
        print("the function was called:", count, "time" if count == 1 else "times")
    return wrap

@call_count
def money():
    pass

# money()
# money()

#6
# def check_authenticity(func):
#     def wrap():
#         if admin:
#             func()
#     return wrap

# admin = True

# @check_authenticity
# def 