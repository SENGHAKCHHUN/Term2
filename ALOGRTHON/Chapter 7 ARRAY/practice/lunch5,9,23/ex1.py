# We have an array2D:
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]

# step1:create function (findPositionOfStar) find the row and column position of capitain
#   result = [1,1] ([row,col])
# def findPositionOfStar(arr):
#     index = None
#     for h in range(len(arr)):
#         for i in range(len(arr[h])):
#             if arr[h][i] == '*':
#                 index = str([h])+str([i])
#     return index
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(findPositionOfStar(array2D))





# step2:create function (moveStartToNextRight) to move the capitain to next right
# def moveStartToNextRight(array):
#     for j in range(len(array)):
#         bool = True
#         for i in range(len(array[j])):
#             if array[j][i] == '*' and bool:
#                 array[j][i] = '0'
#                 array[j][i+1] = '*'
#                 bool = False
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(moveStartToNextRight(array2D))

# def moveStarToNextRight(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == '*' and j < len(array[i])-1:
#                 array[i][j] = '0'
#                 array[i][j+1] = '*'
#             elif array[i][j] == '*' and j == len(array[i])-1:
#                 print("go left")
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# run = True
# while run:
#     command = input("enter ")
#     if command.upper() == 'R':
#         print(moveStarToNextRight(array2D))
#     else:
#         if command == 'stop':
#             print("Finish Action")
#             run = False
#         else:
#             print("unknow " + command +  ' command')
    
    


# array2D = [
#         ['0','0','0'],
#         ['0','0','*'],
#         ['0','0','0']
#     ]



# step3:create function (moveStarToNextLeft) to move the capitain to next left
# array2D = [
#         ['0','0','0'],
#         ['*','0','0'],
#         ['0','0','0']
#     ]

# def moveStarToNextLeft(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == '*' and j > 0:
#                 array[i][j] = '0'
#                 array[i][j-1] = '*'
#             elif array[i][j] == '*' and j == 0:
#                 print("go right")
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# run = True
# while run:
#     command = input("enter ")
#     if command.upper() == 'L':
#         print(moveStarToNextLeft(array2D))
#     else:
#         if command == 'stop':
#             print("Finish Action")
#             run = False
#         else:
#             print("unknow " + command +  ' command')


# def moveStartToNextLeft(array):
#     for j in range(len(array)):
#         bool = True
#         for i in range(len(array[j])):
#             if array[j][i] == '*' and bool:
#                 array[j][i] = '0'
#                 array[j][i-1] = '*'
#                 bool = False
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(moveStartToNextLeft(array2D))



# step4:create function (moveStarToNextUp) to move the capitain to next up
# array2D = [
#         ['0','*','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]

# def moveStarToNextUp(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[j][i] == '*':
#                 array[j-1][i] = '*'
#                 array[j][i] = '0'
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(moveStarToNextUp(array2D))
# def moveStarToNextUp(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j] == '*' and i != 0:
#                 array[i][j] = '0'
#                 array[i-1][j] = '*'
#             elif array[i][j] == '*' and i == 0:
#                 print("go down")
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# run = True
# while run:
#     command = input("enter ")
#     if command.upper() == 'U':
#         print(moveStarToNextUp(array2D))
#     else:
#         if command == 'stop':
#             print("Finish Action")
#             run = False
#         else:
#             print("unknow " + command +  ' command')


# step5:create function (moveStarToNextDown) to move the capitain to next down
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','*','0']
#     ]
# def moveStarToNextDown(array):
#     for j in range(len(array)):
#         bool =True
#         for a in range(len(array[j])):
#             if array[a][j] == '*' and bool:
#                 array[a][j] = '0'
#                 array[a+1][j] = '*'
#                 bool = False
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(moveStarToNextDown(array2D))

# def moveStarToNextDown(array):
#     for i in range(len(array)): 
#         for j in range(len(array[i])):
#             if array[i][j] == '*' and i < len(array)-1:
#                 array[i][j] = '0'
#                 array[i+1][j] = '*'
#             else:
#                 if array[i][j] == '*' and i == len(array)-2:
#                     print("go Up")
#     return array
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# run = True
# while run:
#     command = input("enter ")
#     if command.upper() == 'D':
#         print(moveStarToNextDown(array2D))
#     else:
#         if command == 'stop':
#             print("Finish Action")
#             run = False
#         else:
#             print("unknow " + command +  ' command')


# step6:to check the condition (with user input R or L or U or D)
#   1.If user enter 'R' called the function (moveStartToNextRight) 
#   2.If user enter 'L' called the function (moveStarToNextLeft) 
#   3.If user enter 'U' called the function (moveStarToNextUp)
#   4.If user enter 'D' called the function (moveStarToNextDown) 


def moveStarToNextLeft(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '*' and j > 0:
                array[i][j] = '0'
                array[i][j-1] = '*'
            elif array[i][j] == '*' and j == 0:
                print("go right")
    return array
def moveStarToNextRight(array):
    for i in range(len(array)):
        bool = True
        for j in range(len(array[i])):
            if array[i][j] == '*' and j < len(array[i])-1 and bool:
                array[i][j] = '0'
                array[i][j+1] = '*'
                bool = False
            elif array[i][j] == '*' and j == len(array[i])-1 and bool:
                print("go left")
    return array
def moveStarToNextUp(array):
    for i in range(len(array)):
        bool = True
        for j in range(len(array[i])):
            if array[i][j] == '*' and i > 0 and bool:
                array[i][j] = '0'
                array[i-1][j] = '*'
                bool = False
            elif array[i][j] == '*' and i == 0 and bool:
                print("go down")
    return array
def moveStarToNextDown(array):
    bool = True
    for i in range(len(array)): 
        for j in range(len(array[i])):
            if array[i][j] == '*' and (i < len(array)-1 and bool):
                array[i][j] = '0'
                array[i+1][j] = '*'
                bool = False
            else:
                if array[i][j] == '*' and i == len(array)-1 and bool:
                    print("go Up")
    return array
array2D = [
        ['0','0','0'],
        ['0','*','0'],
        ['0','0','0']
    ]
run = True
while run:
    command = input("enter ")
    if command.upper() == 'L':
        print(moveStarToNextLeft(array2D))
    elif command.upper() == 'R':
        print(moveStarToNextRight(array2D))
    elif command.upper() == 'U':
        print(moveStarToNextUp(array2D))
    elif command.upper() == 'D':
        print(moveStarToNextDown(array2D))
    else:
        if command == 'stop':
            print("Finish Action")
            run = False
        else:
            print("unknow " + command +  ' command')


# step7:print(array2D)