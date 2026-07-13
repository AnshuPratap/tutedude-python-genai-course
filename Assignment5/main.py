#TASK 1:
#1. using module math.utils.py
import math_utils
print(math_utils.add(5,3))
print(math_utils.subtract(5,3))
print(math_utils.square(5))

from math_utils import square, add, subtract
print(square(5))
print(add(5,3))
print(subtract(5,3))

#TASK 2:
#using module string_utils.py
from string_utils import capitalize_words, reverse_string, word_count
print(capitalize_words("hello!! welcome to world"))
print(reverse_string("hello guys"))
print(word_count("hello guys, welcome to the world"))

#TASK 4
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax
print(disc.apply_discount(1000,10))
print(calculate_total([100,200,300]))
print(disc.flat_discount(1000))

total = calculate_total([100,200,300])
print(total)
print(apply_tax(total))
