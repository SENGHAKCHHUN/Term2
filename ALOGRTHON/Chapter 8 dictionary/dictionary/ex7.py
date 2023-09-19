# Ex6 - Array 2D
# arr2D = [
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0']
# ]
# def gridNumber(array):
#     string = ''
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             string += array[i][j] + ' ' 
#         string += '\n'
#     return string
# arr2D = [
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0']
# ]
# print(gridNumber(arr2D))
# Display result in console:
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0


def stringNumber(array):
    string = ''
    for i in range(len(array)):
        for j in range(len(array[i])):
            string += array[i][j] + '  '
        string += '\n'
    return string
arr2D = [
  ['❤️','❤️','❤️','❤️'],
  ['❤️','❤️','❤️','❤️'],
  ['❤️','❤️','❤️','❤️'],
  ['❤️','❤️','❤️','❤️']
]
print(stringNumber(arr2D))