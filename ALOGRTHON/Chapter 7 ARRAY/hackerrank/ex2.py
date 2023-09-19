def findIndexOfSeven(array):
    index = 0
    for i in range(len(array)):
        if array[i] == 7:
            index = i
    array.pop(index)
    return array
array = eval(input())
print(findIndexOfSeven(array))
