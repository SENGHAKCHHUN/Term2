def sumBetweenNumberTwo(number):
    isFound = False
    sum = 0
    for i in range(len(number)):
        if (number[i]) == 2 and not isFound:
            isFound = True
        elif isFound and (number[i]) != 2:
            sum += int(number[i])
    return sum
number = eval(input())
print(sumBetweenNumberTwo(number))