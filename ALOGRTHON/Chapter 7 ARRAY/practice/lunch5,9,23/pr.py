# We have an array2D:
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]

# step1:create function (findPositionOfStar) find the row and column position of capitain
#   result = [1,1] ([row,col])

# def findPositionOfStar(array):
#     positionStar = []
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[j][i] == '*':
#                 positionStar.append(i)
#                 positionStar.append(j)
#     return positionStar
# array2D = [
#         ['0','0','0'],
#         ['0','*','0'],
#         ['0','0','0']
#     ]
# print(findPositionOfStar(array2D))


# step2:create function (moveStartToNextRight) to move the capitain to next right
# array2D = [
#         ['0','0','0'],
#         ['0','0','*'],
#         ['0','0','0']
#     ]

def findPositionOfStar(array):
    positionStar = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '*':
                positionStar.append(i)
                positionStar.append(j)
    print(positionStar)
    return positionStar
def moveLeft(arr,row,col):
    arr[row][col] = '0'
    arr[row][col -1] = '*'
    return arr
def moveRight(arr,row,col):
    arr[row][col] = '0'
    arr[row][col +1] = '*'
    return arr
def moveUp(arr,row,col):
    arr[row][col] = '0'
    arr[row-1][col] = '*'
    return arr
def moveDown(arr,row,col):
    arr[row][col] = '0'
    arr[row+1][col] = '*'
    return arr
array2D = [
        ['0','0','0'],
        ['0','*','0'],
        ['0','0','0']
]
startAction = True
while startAction:
    currentPosition = findPositionOfStar(array2D)
    command = input('enter ')
    row = currentPosition[0]
    col = currentPosition[1]
    if command.upper() == 'L':
        print(moveLeft(array2D,row,col))
    elif command.upper() == 'R':
        print(moveRight(array2D,row,col))
    elif command.upper() == 'U':
        print(moveUp(array2D,row,col))
    elif command.upper() == 'D':
        print(moveDown(array2D,row,col))
    elif currentPosition[0]:
        print("Go right")
    else:
        if command == 'stop':
            print("Finish Action")
            startAction = False
        else:
            print("Unknown " + command + ' command')





# step3:create function (moveStarToNextLeft) to move the capitain to next left
# array2D = [
#         ['0','0','0'],
#         ['*','0','0'],
#         ['0','0','0']
#     ]

# step4:create function (moveStarToNextUp) to move the capitain to next up
# array2D = [
#         ['0','*','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]

# step5:create function (moveStarToNextDown) to move the capitain to next down
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','*','0']
#     ]

# step6:to check the condition (with user input R or L or U or D)
#   1.If user enter 'R' called the function (moveStartToNextRight) 
#   2.If user enter 'L' called the function (moveStarToNextLeft) 
#   3.If user enter 'U' called the function (moveStarToNextUp)
#   4.If user enter 'D' called the function (moveStarToNextDown) 
 
# step7:print(array2D)