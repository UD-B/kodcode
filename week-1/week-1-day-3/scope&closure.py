# 1.1
def power_of(n):
    def power(x):
        return x ** n
    return power
# power_of_4 = power_of(4)
# print(power_of_4(2))

# 1.2
def power_of(n):
    def power():
        return n ** n
    return power()
# print(power_of(4))


# 2.
def outer_counter():
    count = 0
    def inner_counter():
        nonlocal count
        count += 1
        print(count)
    return inner_counter
count = outer_counter()
count()
count()