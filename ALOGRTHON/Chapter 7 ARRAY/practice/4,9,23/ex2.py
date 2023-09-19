
# Ex2:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

# output:
# [2, 3]
# [4, 3, 1]

def reverse(array):
    res = 0
    newarr = []
    for i in range(len(array)):
        res = array[-1-i]
        newarr.append(res)
    return newarr
Number = int(input())
result = ''
for i in range(Number):
    value = eval(input())
    result = reverse(value)
    print(result)