# Ex2 - Array 2D
arr2D = [
  [1, 2, 3],
  [3, 5, 9],
  [8, 4, 3]
]
#1 - Sum each array
# [6, 17, 15]

# number = ''
# for i in range(len(arr2D)):
#     number =(arr2D[i])
#     sum = 0
#     for j in range(len(number)):
#         sum += (number[j])
#     arr2D[i] = sum
# print(arr2D)

#2 - Select only odd number
# [1, 3, 3, 5, 9, 3]
# newarr = []
# number = ''
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     for j in range(len(number)):
#         if number[j] % 2 != 0:
#             newarr.append(number[j])
# print(newarr)



#3 - Replace all odd number with 168
# [
#   [168, 2, 168],
#   [168, 168, 168],
#   [8, 4, 168]
# ]
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     for j in range(len(number)):
#         if number[j] % 2 != 0:
#             number[j] = 168
# print(arr2D)