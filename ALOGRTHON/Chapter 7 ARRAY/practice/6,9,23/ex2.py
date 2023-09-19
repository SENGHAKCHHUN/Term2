# def makeArray2D(row,col):
#     newarr = []
#     string = ''
#     for i in range(row):
#         newarr.append([])
#         for j in range(col):
#             newarr[i].append('0')
#         string += str(newarr[i]) + '\n'
#     return string
# row = int(input('Enter row '))
# col = int(input('Enter column '))
# print(makeArray2D(row,col))

def createArray(col):
    res = ''
    for i in range(col):
        res += '*'
    return res
def displayGrid(Grid):
    result = ''
    for i in range(len(Grid)):
        for j in range(len(Grid[i])):
            result += Grid[i][j] + ' '
        result += '\n'
    return result
row = int(input('Enter row '))
col = int(input('Enter column '))
arr2D = []
for i in range(row):
    arr2D.append(createArray(col))
print(arr2D)
print(displayGrid(arr2D))
