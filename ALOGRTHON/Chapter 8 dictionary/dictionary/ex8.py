# Ex7 - Array 2D
# arr2D = [
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','*','0'],
#   ['0','0','0','0']
# ]
#Where is index of "*"
# output: [2, 2]
def positonOfIndex(array):
    positionList = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '*':
                positionList.append(i)
                positionList.append(j)
    return positionList
arr2D = [
  ['0','0','0','0'],
  ['0','0','0','0'],
  ['0','0','*','0'],
  ['0','0','0','0']
]
print(positonOfIndex(arr2D))