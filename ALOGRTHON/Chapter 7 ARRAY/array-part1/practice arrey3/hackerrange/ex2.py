def findIndexOfSeven(array):
    index = 0
    arrList = []
    for i in range(len(array)):
        if int(array[i]) != 7:
            arrList.append(array[i])
    return arrList
number = eval(input())
print(findIndexOfSeven(number))