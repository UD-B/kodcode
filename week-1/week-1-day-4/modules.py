#1
from math_utils import add, multiply

# print(add(1, 2))
# print(multiply(1, 2))


#2
import random
def random_generator():
    rand_list = []
    for i in range(0, 5):
        random_int = random.randint(1, 100)
        rand_list.append(random_int)
    return rand_list
# print(random_generator())

#3
import math as m
# print(m.sqrt(16))

#4
from math import pi
circle_radius = 5
circle_area = pi * 5 ** 2
# print(circle_area)

#5
from string_utils import reverse_string as reverse
from string_utils import is_palindrome as palindrome
print(reverse("not a ton"))
print(palindrome("not a ton"))

