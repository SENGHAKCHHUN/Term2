# Ex1 - Array
# input1: hello
# output: olleh
# string = input()
# res = ''
# for i in range(len(string)):
#     res += string[-1-i]
# print(res)



# -----
# Ex2 - Array
# input1: hello
# output: ['o','l','l','e','h']
# list = []
# string = input()
# for i in range(len(string)):
#     list.append(string[-1-i])
# print(list)



# -----
# Ex3 - Array
# input1: ['banana','coconut']
# ouput: ['ananab','tunococ']
# def reverWord(word):
#     res = ''
#     for i in range(len(word)):
#         res += word[-1-i]
#     return res
# array = eval(input())
# for i in range(len(array)):
#     array[i] = reverWord(array[i])
# print(array)



# ----
# Ex4 - Array use only 1 function
# Case 1:
# input: [1, 3, 4, 4]
# input: odd
# output: 4

# Case 2:
# input: [1, 3, 4, 4]
# input: even
# output: 8

# case 3:
# input: [1, 3, 4, 4]
# input: add
# output: Command not found
# def sumNumber(array,value):
#     sum = 0
#     if value == 'even':
#         num = 0
#     else:
#         num = 1
#     for i in range(len(array)):
#         if array[i] % 2 == num:
#             sum += array[i]
#     return sum
# array = eval(input())
# command = input("enter command")
# if command == 'even':
#     print(sumNumber(array,command))
# elif command == 'odd':
#     print(sumNumber(array,command))
# else:
#     print("command not found")
    



# -----
# Ex5 - Array
# input: ['banana', 'coconut']
# output: 
# [
#   {'b': 1},
#   {'a': 3},
#   {'n': 3},
#   {'c': 2},
#   {'o': 2},
#   {'u': 1},
#   {'t': 1},
# # ]

def checkValue(list,value):
    isTrue = True
    for i in range(len(list)):
        for key in list[i]:
            if key == value:
                isTrue = False
    return isTrue
def count(arr,value):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if value == arr[i][j]:
                count +=1
    return count    
arr = eval(input("enter mk jam "))
list = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        obj = {}
        if checkValue(list,arr[i][j]):
            list.append(obj)
        obj[arr[i][j]] = count(arr,arr[i][j])
print(list)


# def count(arr,value):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if value == arr[i][j]:
#                 count +=1
#     return count    
# arr = eval(input("enter mk jam "))
# list = []
# obj = {}
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         obj[arr[i][j]] = count(arr,arr[i][j])
# list.append(obj)
# print(list)
























# def count(array):
#     count = 0
#     value = array[i]
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == value:
#                 count +=1
#     return count
# array = eval(input())
# for i in range(len(array)):
#     obj = {}
#     for h in range(len(array[i])):
#         for k in range(len(array[i][h])):
#             obj[array[h]] = count(array,array[i][h][k])
#             print(array[i][h][k])
# print(obj)
        
        


    