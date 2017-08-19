
from random import random

ran_num = [1,3,45,56,32,23,123,13,15,8,14]
for i in ran_num:
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz-Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
