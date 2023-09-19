def checkNumber(value,number):
    bool = True
    for i in range(len(number)):
        if value == number[i]:
            bool = False
    return bool
array = eval(input())
number = []
for i in range(len(array)):
    if checkNumber(array[i],number):
        number.append(array[i])
print(number)