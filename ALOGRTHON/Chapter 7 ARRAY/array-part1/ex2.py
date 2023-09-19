def getIndexMinNumber(Number):
    res = 0
    if len(Number) != 0:
        isSmall = int(Number[0])
        for i in range(len(Number)):
            if int(Number[i]) < isSmall:
                isSmall = Number[i]
                res = i
        return res
    return None
number = eval(input())
print(getIndexMinNumber(number))

