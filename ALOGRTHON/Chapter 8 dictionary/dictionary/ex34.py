# Ex1: 
arr = ['0', '0', 'x', '0', '0', '0', '0']

#1 - Find index of x
# index = None
# for i in range(len(arr)):
#     if arr[i] == 'x':
#         index = i
# print(index)


#2 - Replace x by 0 and replace 0 by x
# for i in range(len(arr)):
#     if arr[i] == '0':
#         arr[i] = 'x'
#     elif arr[i] == 'x':
#         arr[i] = '0'
# print(arr)


#3 - Move x to next position
#   ['0', '0', '0', 'x', '0', '0', '0']
# i = 0
# bool = False
# while i < len(arr) and not bool:
#     if arr[i] == 'x':
#         arr[i] = '0'
#         arr[i+1] = 'x'
#         bool = True
#     i +=1
# print(arr)

#4 - Move x to prevouis position
#   ['0', 'x', '0', '0', '0', '0', '0']
# i = 0
# bool = False
# while i < len(arr) and not bool:
#     if arr[i] == 'x':
#         arr[i] = '0'
#         arr[i-1] = 'x'
#         bool = True
#     i +=1
# print(arr)

# -------------------------------------------  
# Ex2 
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# Enter: right
# To move x to right
# ['0', '0', '0', 'x', '0', '0', '0']
def positionOfX(arr):
    bool = True
    index = None
    for i in range(len(arr)):
        if arr[i] == 'x' and bool:
            index = i 
            bool = False
    return index
def moveLeft(arr,currentPositon):
    arr[currentPositon-1] = 'x'
    arr[currentPositon] = '0'
    return arr
def moveright(arr,currentPositon):
    arr[currentPositon+1] = 'x'
    arr[currentPositon] = '0'
    return arr
arr = ['0', '0', 'x', '0', '0', '0', '0']
isRun = True
while isRun:
    currentPositon = positionOfX(arr)
    command = input("enter jam kal ")
    if command == 'r':
        print(moveright(arr,currentPositon))
    elif command == 'l':
        print(moveLeft(arr,currentPositon))
# Enter: left
# To move x to left
# ['0', 'x', '0', '0', '0', '0', '0']
# ------------------------------------------
# Ex3
arr = [
  ['0', 'x', '0', '0'],
  ['0', '0', '0', '0'],
  ['0', '0', '0', '0'],
  ['0', '0', '0', '0'],
  ['0', '0', '0', '0']
]
#1 - Where is the position of x
#2 - Move x to last index in first row
#  [
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
#3 Move x to below
#  [
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]

# Laaty, [9/12/2023 7:32 PM]
# Ex1:
# number of array: 3
# > [3, 3]
# > [1, 3, 4]
# > [4, 5, 9, 1]

# output:
# 6
# 8
# 19
# ———————————————-
# Ex2:
# number of array: 2
# > [3, 2]
# > [1, 3, 4]

# output:
# [2, 3]
# [4, 3, 1]

# Laaty, [9/12/2023 7:33 PM]
# Ex4 - Array 2D
# arr2D = [
#   [1, 2, 3],
#   [2, 3, 5],
#   [4, 5, 8],
#   [4, 3, 1]
# ]
#1 - How many row and column
# result: 4 rows 3 columns
#2 - Replace number < 3 with 9
# [
#   [9, 9, 3],
#   [9, 3, 5],
#   [4, 5, 8],
#   [4, 3, 9]
# ]
#3 - Sum row value in arr2D
# [6, 10, 17, 8]
#4 - Sum columns
# [11, 13, 17]

# Laaty, [9/12/2023 7:34 PM]
# Ex3 - Array
# arr = [6, 4, 3, 4]
#1 - Sum first index with last  index
# result = 10
#2 - Square all number (function)
# [36, 16, 9, 16]
#3 - Remove duplicate from list (function)
# [6, 3, 4]
#4 - create 2D array follow number in list
# [
#   [1, 2, 3, 4, 5, 6],
#   [1, 2, 3, 4]
#   [1, 2, 3],
#   [1, 2, 3, 4]
# ]

# Laaty, [9/12/2023 7:34 PM]
# Ex1 - String
# text = "banana"
#1 - How many letter in string
#2 - How many letter "A" in string
#3 - Reverse string
#4 - Convert all letter to uppercase except letter "A"

# -----------------------
# Ex2 - Array
# arr = [1000, 200, 404, 500, 10]
#1 - How many degit of each item
# [4, 3, 3, 3, 2]
#2 - Remove 404 from list
#3 - Reverse array
# [10, 500, 404, 200, 1000]
#4 - Sum only number with last degit is 0
# result: 1710

# Laaty, [9/12/2023 7:34 PM]
# Ex1 - Array string
# arr = ['banana','coconut','mango','jackfruit']

#1 - Count letter each item (function)
# [6,7,5,9]

#2 - Reverse string in list (function)
# ['ananab', 'tunococ', ...]

#3 - Count letter "n" in list (function)
# [2, 1, 1, 0]

#4 - Get last letter in each item (function)
# ['a', 't', 'o', 't']

#5 - Add new fruit to list (function)
# function name: addNewFruit(arr, newFruit)
# ['banana','coconut','mango','jackfruit', 'orange']

#6 - Concate first text together
# bcmj
# 
# Laaty, [9/12/2023 7:34 PM]
# Ex7 - Array (while only)
# arr = [1024, 1010, 2024, 123454]
#1 - How many degit each item
# [4, 4, 4, 6]
#2 - Sum each number in each value together (1 + 0 + 2 + 4)
# [7, 2, 8, 19]
#3 - Sum only last degit number on each item (4 + 0 + 4 + 4)
sum = 12

# Laaty, [9/12/2023 7:34 PM]
# Ex5 - Array (While loop only)
# arr = ['A','A','B','B','C','A','C']
#1 - Create to new list to remove duplicate value
#2 - If A = 10, B = 20, C = 30 how many value in list in total
#3 - Filter new list and keep letter "A" only

# Ex6 - Array (While loop only)
# arr = [1, 10, 168, 190, 2024, 120393]
#1 - Remove 2024 from list
#2 - How many degit from each item
# [1, 2, 3, 3, 4, 6]
#3 - replace all item that have degit greater than 3 by 100
# [1, 10, 100, 100, 100, 100]