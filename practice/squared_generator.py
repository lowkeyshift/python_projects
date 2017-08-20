

def nums_squared(nums):
    for i in nums:
        yield(i*i)

my_nums = nums_squared([1, 5, 9, 22, 35, 68, 93, 47, 100, 200, 33454])

for num in my_nums:
    print(num)
