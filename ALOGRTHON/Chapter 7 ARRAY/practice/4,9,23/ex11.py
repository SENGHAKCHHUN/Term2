# Ex1: 
# arr = ['0', '0', 'x', '0', '0', '0', '0']

#1 - Find index of x
# for i in range(len(arr)):
#     if arr[i] == 'x':
#         print(i)



#2 - Replace x by 0 and replace 0 by x
# for i in range(len(arr)):
#     if arr[i] == 'x':
#         arr[i] = '0'
#     elif arr[i] == '0':
#         arr[i] = 'X'
# print(arr)


#3 - Move x to next position
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# bool = False
# #   ['0', '0', '0', 'x', '0', '0', '0']
# for i in range(len(arr)):
#     if arr[i] == 'x' and len(arr)-1 > i and not bool:
#         arr[i+1] = 'x'
#         arr[i] = '0'
#         bool = True
# print(arr)

# def indexOfX(array):
#     index = None
#     for i in range(len(array)):
#         if array[i] == 'x':
#             index = i
#     return index
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# currentIndex = indexOfX(arr)
# arr[currentIndex]  ='0'
# arr[currentIndex+1] = 'x'
# print(arr)
    
#4 - Move x to prevouis position
#   ['0', 'x', '0', '0', '0', '0', '0']
# for i in range(len(arr)):
#     if arr[i] == 'x':
#         arr[i-1] = 'x'
#         arr[i] = '0'
# print(arr)


# def indexOfX(array):
#     index = None
#     for i in range(len(array)):
#         if array[i] == 'x':
#             index = i
#     return index
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# currentIndex = indexOfX(arr)
# arr[currentIndex]  ='0'
# arr[currentIndex-1] = 'x'
# print(arr)

# -------------------------------------------  
# Ex2 
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# Enter: right
# To move x to right
# ['0', '0', '0', 'x', '0', '0', '0']

# Enter: left
# To move x to left
# ['0', 'x', '0', '0', '0', '0', '0']
arr = ['0', '0', 'x', '0', '0', '0', '0']
bool = False
while not bool:
  run = input("enter ")
  if run == 'left':
    isEat = True
    for j in range(len(arr)):
      if arr[j] == 'x'and j > 0:
        arr[j-1] = 'x'
        arr[j] = '0'
      elif arr[j-1] == 'x' and isEat:
        arr[j] = 'x'
        arr[j-1] = '0'
        isEat = False
    print(arr)
  elif run == 'right':
    isEat = True
    for j in range(len(arr)):
      if arr[j-1] == 'x' and isEat and j > 0:
        arr[j] = 'x'
        arr[j-1] = '0'
        isEat = False
      elif arr[len(arr)-1] == 'x':
        arr[len(arr)-2] = 'x'
        arr[len(arr)-1] = '0'
        print(arr[len(arr)-1])
        print(arr[len(arr)-2])
        isEat = True
    print(arr)
  elif run == 'stop' or run == 'Stop':
    bool = True


# ------------------------------------------
# Ex3
# arr = [
#   ['0', 'x', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]

#1 - Where is the position of x
# for i in range(len(arr)):
#   index = None
#   for j in range(len(arr[i])):
#     if arr[i][j] == 'x':
#       index = str([i])+ str([j])
#       print(index)




#2 - Move x to last index in first row
#  [
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
# row = len(arr)
# coloum = len(arr[0])
# for i in range(row):
#   for j in range(coloum-1):
#     if arr[i][j] == 'x':
#       arr[i][coloum-1] = 'x'
#       arr[i][j] = '0'
# print(arr)

            
  
#3 Move x to below
#  [
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
# arr = [
#   ['0', 'x', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
# row = len(arr)
# coloum = len(arr[0])
# bool = False
# for i in range(coloum):
#   for j in range(row):
#    if arr[j][i] == 'x' and not bool:
#       Index = arr[j][i]
#       arr[j][i] = '0'
#       arr[j+1][i] = Index
#       bool = True      
# print(arr)
