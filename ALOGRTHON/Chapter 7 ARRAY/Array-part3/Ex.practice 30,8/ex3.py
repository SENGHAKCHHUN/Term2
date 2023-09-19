# Ex3 - Array 2D
arr2D = [
  [1, 2, 3],
  [3, 5, 9],
  [8, 4, 3]
]

sum = 0
newlist = []
n = ''
for i in range(len(arr2D)):
    n = arr2D[i]
    for j in range(len(n)):
        sum += arr2D[i][j]
    newlist.append(sum)
    sum = 0
print(newlist)

# sum = 0
# newList = []
# for i in range(len(arr2D)):
#     for j in range(len(arr2D[i])):
#         sum += arr2D[j][i]
#     newList.append(sum)
#     sum = 0
# print(newList)

# m=0
# sumarr=[]
# while m<len(arr2D):
#     sum=0
#     for i in range(len(arr2D)):
#         n=arr2D[i]
#         for j in range(len(n)):
#             if j==m:
#                 sum+=n[j]
#     sumarr.append(sum)
#     m+=1
# print(sumarr)


#1 - sum in column
# [12, 11, 15]
# number = ''
# sum1 = 0
# sum2 = 0
# sum3 = 0
# newarr = []
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     for j in range(len(number)):
#         if j == 0 :
#             sum1 += number[j]
#         elif j == 1:
#             sum2 += number[j]
#         elif j == 2:
#             sum3 += number[j]
# newarr.append(sum1)
# newarr.append(sum2)
# newarr.append(sum3)
# print(newarr)





# 2 - sum first column 
# number = ''
# sum = 0
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     sum += number[0]
# print(sum)
# result: 12




#3 - sum last column
# result: 15
# sum =0 
# number = ''
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     sum += number[len(number)-1]
# print(sum)



# 4 How many row and column in this array 2D
# result: 3 rows 3 columns
# number = ''
# row = 0
# coloum = 0
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     # row = 0
#     for j in range(len(number)):
#         row += 1
#     coloum +=1
# print(str(row)+ " rows " + str(coloum) + " coloums")


#5 Find index of 9
# index = 0
# number = ''
# for i in range(len(arr2D)):
#     number = arr2D[i]
#     for j in range(len(number)):
#         if number[j] == 9:
#             index = j
# print(index)
# result: 2