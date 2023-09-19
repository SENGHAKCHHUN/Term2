def sumArray(array) :
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
array1 = eval(input())
array2 = eval(input())
print(sumArray(array1))
print(sumArray(array2))