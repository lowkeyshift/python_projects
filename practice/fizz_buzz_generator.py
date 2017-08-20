 Change the count size to play the FizzBuzz game to what ever limit you choose
# The count starts at 0 and end at 99
count_size = 100
for i in range(count_size):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz-Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
