# Ex1 - Array
# String to array
# Input: Hello
# Output: ['H','e','l','l','o']
# string = input("enter word")
# list = []
# for i in range(len(string)):
#     list.append(string[i])
# print(list)


# ------------------
# Ex2 - Array
# String to array seperate by space
# Input: aba bank in Cambodia
# output: ['aba', 'bank','in','Cambodia']
# string = input("enter sentence ")
# list = []
# word = ''
# for i in range(len(string)):
#     if string[i] == ' ' or len(string)-1 == i:
#         if len(string)-1 == i:
#             word += string[i]
#         list.append(word)
#         word = ''
#     else:
#         word += string[i]
# print(list)



# ------------------
# Ex3 - Array
# Get only text contains letter A
# Input: ['banana','coconut','mango']
# output: ['banana','mango']
# arr = eval(input('enter arr '))
# list = []
# for i in range(len(arr)):
#     bool = False
#     for j in range(len(arr[i])):
#         if arr[i][j] == 'a' and not bool:
#             list.append(arr[i])
#             bool = True
# print(list)


# ------------------
# Ex4 - Array
# Reverse array and reverse text in array
# Input: ['banana','coconut']
# output: 
# ['coconut','banana']
# ['ananab','tunococ']

# def reverseText(word):
#     res = ''
#     for i in range(len(word)):
#         res += word[-1-i]
#     return res
# arr = eval(input("enter array "))
# listReversed = []
# listTextReverse = []
# for i in range(len(arr)):
#     listReversed.append(arr[-1-i])
#     listTextReverse.append(reverseText(arr[i]))
# print(listReversed)
# print(listTextReverse)




# ------------------
# Ex5 - Array
#Count number
# Input1: [2, 2, 3, 5, 2, 3, 2, 5, 8]
# Input2: [2, 3]
# Output: [ { 2: 4} , {3: 2} ]

# def countNumber(listN ,value):
#     count = 0
#     for i in range(len(listN)):
#         if listN[i] == value:
#             count +=1
#     num = {}
#     num[value] = count
#     return num
# N1arr = eval(input("enter arr"))
# NFind = eval(input("enter find number"))
# res = []
# for i in range(len(NFind)):
#     res.append(countNumber(N1arr, NFind[i]))
# print(res)


# ------------------
# Ex6 - Array
# Array to object
# input: ['banana','coconut', 'mango', 'orange']
# output: 
# [
#   {0: 'banana',1: 'coconut',2: 'mango',3: 'orange'}
# ]
# array = eval(input("enter array"))
# list = []
# for i in range(len(array)):
#     num = {}
#     num[i] = array[i]
#     list.append(num)
# print(list)


# --------------
# Ex7 - Array
# Array to object - counting character
# input: ['banana','coconut', 'mango', 'orange']
# output: 
# [
#   {'banana':6,'coconut':7,'mango': 5,'orange': 6}
# ]
array = eval(input("enter array"))
list = []
for i in range(len(array)):
    n = len(array[i])
    obj = {}
    obj[array[i]] = n
    list.append(obj)
print(list)
# --------------