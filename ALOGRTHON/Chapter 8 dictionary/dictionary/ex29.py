# Ex7 - Array 2D
# input: [3,4, 5, 1]
# ouput: 
# [
#   [1, 2, 3],
#   [1, 2, 3, 4],
#   [1, 2, 3, 4, 5],
#   [1]
# ]
def makeNum(value):
    list = []
    for i in range(value):
        list.append( i + 1)
    return list
array = eval(input("enter one array "))
newArr = []
for k in range(len(array)):
    newArr.append(makeNum(array[k]))
print(newArr)
