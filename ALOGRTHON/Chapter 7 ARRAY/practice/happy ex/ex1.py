# list1 = eval(input())
# list2 = eval(input())
# newlist = []
# if len(list1) >= len(list2):
#     i = 0
#     while i < len(list1):
#         if len(list1) > i:
#             newlist.append(list1[i])
#         if len(list2) > i:
#             newlist.append(list2[i])
#         i +=1
#     print(newlist)
# elif len(list1) == 0 and len(list2) == 0:
#     print("EMPTY")
# elif len(list1) < len(list2):
#     i = 0
#     while i < len(list2):
#         if len(list1) > i:
#             newlist.append(list1[i])
#         if len(list2) > i:
#             newlist.append(list2[i])
#         i +=1   
#     print(newlist)




# def average(scores):
#     sum = 0
#     for i in range(len(scoreS)):
#         sum += scoreS[i]
#     average = sum / len(scoreS)
#     return average
# student = int(input())
# total = 0
# for i in range(student):
#     scoreS = eval(input())
#     res = average(scoreS)
#     total += res
# print(total/student)
  

# def CountChar(word, char):
#     count = 0
#     for j in range(len(word)):
#         if word[j] == char:
#             count += 1
#     return count 
# words = eval(input())
# character = input()
# count = 0
# letter = ''
# for i in range(len(words)):
#     letter = words[i]
#     count += CountChar(letter,character)
# print(count)


# def multiplyWithinRange(startNumber, res):
#     multiply = res * startNumber
#     return multiply    
# startNumber = int(input())
# endNumber = int(input())
# i = startNumber
# res = 1
# if startNumber < endNumber:
#     while i <= endNumber:
#         res = multiplyWithinRange(startNumber,res)
#         startNumber += 1
#         i += 1
#     print(res)
# else:
#     print(0)


# bool = False
# i = 0
# while i < 3 and not bool:
#     number = int(input())
#     if number!= 72 and i < 2:
#         print("again")
#     elif number == 72:
#         print("win")
#         bool = True
#     elif i == 2 and number!= 72:
#         print("lost")
#     i +=1


# Enter your code here. Read input from STDIN. Print output to STDOUT
# array2D = eval(input())
# newarr = []
# row = len(array2D)
# coloum = len(array2D[0])
# for i in range(row):
#     max = array2D[i][0]
#     for j in range(coloum):
#         if max < array2D[i][j]:
#             max =  array2D[i][j]
#     newarr.append(max)
# print(newarr)



# array2D = eval(input())
# newarr = [] 
# for i in range(len(array2D)):
#     min = array2D[j][0]
#     for j in range(len(array2D[i])):
#         if min > array2D[i][j]:
#             min = array2D[i][j]
#     newarr.append(min)
# print(newarr)
# array2D = [
#   [1, 2, 3],
#   [3, 5, 9],
#   [8, 4, 3]
# ]
# newarr=[]
# column = len(array2D[0])
# row = len(array2D)
# for i in range(column):
#   min = array2D[0][i]
#   for j in range(row):
#     if min > array2D[j][i]:
#         min = array2D[j][i]
#   newarr.append(min)
# print(newarr)


# newarr=[]
# column = len(arr2D[0])
# row = len(arr2D)
# for i in range(column):
#   sum = 0
#   for j in range(row):
#     sum += arr2D[j][i]
#   newarr.append(sum)
# print(newarr)
# print(arr2D[j][i])   


# array = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [4,1,5],
#     [5,2,6]
# ]
# newarr = []
# row = len(array)
# coloum = len(array[0])
# for i in range(row):
#     sum = 1
#     for j in range(coloum):
#         sum += array[i][j]
#     newarr.append(sum)
# print(newarr)



# array = [
#     [1,2,3],
#     [4,5,1],
#     [1,8,9],
#     [3,7,1]
# ]
# row = len(array)
# coloum = len(array[0])
# newarr = []
# count = 0
# for i in range(coloum):
#   for j in range(row):
#    if array[j][i] == 3:
#     count += array[j][i]
# print(count)






# n=2
# n1=5
# sum=1
# for i in range(n1):
#     sum*=n
# print(sum)