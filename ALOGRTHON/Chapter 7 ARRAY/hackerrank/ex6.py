# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkNumber(value,number):
    bool = True
    for i in range(len(number)):
        if str(value) == number[i]:
            bool = False
    return bool
array = eval(input())
number = ''
for i in range(len(array)):
    if checkNumber(array[i],number):
        number += str(array[i]) + " "
print(number)