def sumOddEvenNumber(array):
    odd = 0
    even = 0
    for i in range(len(array)):
        if int(array[i])%2 ==0:
            even+= int(array[i])
        else:
            odd += int(array[i])
    res = "sum of Even is "+ str(even) + ", and sum of Odd is " + str(odd)
    return res
listArray = eval(input())
print(sumOddEvenNumber(listArray))


