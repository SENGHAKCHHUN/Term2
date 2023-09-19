def checkNumber(number):
    isFound = False
    i = 0
    while i < len(number) and not isFound:
        if number[i] > 10 and number[i]<=16:
            isFound = True
        i +=1
    return isFound
number = eval(input())
print(checkNumber(number))