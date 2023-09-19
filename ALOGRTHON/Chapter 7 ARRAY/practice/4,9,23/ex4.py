# Ex4:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

# output:
# [9, 4]
# [1, 9, 16]
def square(value):
    return value * value
number = int(input())
for i in range(number):
    list = eval(input())
    for j in range(len(list)):
        list[j] = square(list[j])
    print(list)