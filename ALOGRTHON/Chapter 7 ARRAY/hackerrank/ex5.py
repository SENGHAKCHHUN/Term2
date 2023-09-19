def replaceZero(array):
    for i in range(len(array)):
        if array[i] == 1:
            array[i] = 0
    return array
array = eval(input())
print(replaceZero(array))