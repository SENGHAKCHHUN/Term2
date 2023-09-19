# Ex4 - Array 2D
arr2D = [
  [1, 2, 3],
  [2, 3, 5],
  [4, 5, 8],
  [4, 3, 1]
]
#1 - How many row and column
# coloum = 0
# for i in range(len(arr2D)):
#     row = 0
#     for j in range(len(arr2D[i])):
#         row+=1
#     coloum +=1
# print(str(coloum) + " coloums " + str(row) + " rows ")
# result: 4 rows 3 columns


#2 - Replace number < 3 with 9
# for i in range(len(arr2D)):
#     n = arr2D[i]
#     for j in range(len(n)):
#         if n[j] < 3:
#             n[j] = 9
#     print(arr2D)
# [
#   [9, 9, 3],
#   [9, 3, 5],
#   [4, 5, 8],
#   [4, 3, 9]
# ]

#3 - Sum row value in arr2D
# sum = 0
# newlist = []
# for j in range(len(arr2D)):
#     for i in range(len(arr2D[j])):
#         sum += arr2D[j][i]
#     newlist.append(sum)
#     sum = 0
# print(newlist)
# [6, 10, 17, 8]



#4 - Sum columns
# [11, 13, 17]
arr2D = [
  [1, 2, 3],
  [2, 3, 5],
  [4, 5, 8],
  [4, 3, 1]
]
sum = 0
newlist = []
for j in range(len(arr2D)-1):
    for i in range(len(arr2D[j])+1):
        sum += arr2D[i][j]
    newlist.append(sum)
    sum = 0
print(newlist)
