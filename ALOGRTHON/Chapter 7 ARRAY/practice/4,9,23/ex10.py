# Ex10
# From list of array 2D
# numbers = [
#   [1,3,4, 4],
#   [3, 4, 0, 4]
#   [5, 6, 9, 0]
#   [4, 5, 9, 7]
# ]
#1 - How many number 4 from array 2D (function)
# def findNumberfour(array):
#     count = 0
#     for i in range(len(array)):
#         if array[i] == 4:
#             count +=1
#     return count
# numbers = [
#   [1, 3, 4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# total = 0
# for j in range(len(numbers)):
#     res = findNumberfour(numbers[j])
#     total += res
# print(total)



#2 - Sum each list of array in array 2D (function)
# output: [12, 11, 20, 25]
def sumNumber(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
numbers = [
  [1, 3, 4, 4],
  [3, 4, 0, 4],
  [5, 6, 9, 0],
  [4, 5, 9, 7]
]
newarr = []
res = 0
for i in range(len(numbers)):
    res = sumNumber(numbers[i])
    newarr.append(res)
print(newarr)


#3 - Sum only number 4 in list 
# def sumNumber(array):
#     sum = 0
#     for i in range(len(array)):
#         num = array[i]
#         for j in range(len(num)):
#             if num[j] == 4:
#                 sum += num[j]
#     return sum
# numbers = [
#   [1, 3, 4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# print(sumNumber(numbers))


#4 - Replace number 0 with 99 (function)

# def sumNumber(array):
#     sum = 0
#     for i in range(len(array)):
#         num = array[i]
#         for j in range(len(num)):
#             if num[j] == 0:
#                 num[j] = 99
#     return array
# numbers = [
#   [1, 3, 4, 4],
#   [3, 4, 0, 4],
#   [5, 6, 9, 0],
#   [4, 5, 9, 7]
# ]
# print(sumNumber(numbers))


#5 - where find index of 7 in list
def sumNumber(array):
    res = ''
    for i in range(len(array)):
        num = array[i]
        for j in range(len(num)):
            if num[j] == 7:
                res = str([i]) + str([j])
    return res
numbers = [
  [1, 3, 4, 4],
  [3, 4, 0, 4],
  [5, 6, 9, 0],
  [4, 5, 9, 7]
]
print(sumNumber(numbers))
# output: [3][3]