def average(array):
    sum = 0
    average = 0
    total = 0
    n = len(array)
    for i in range(len(array)):
        sum += int(array[i])
    total = sum / n
    return total
numberOfStu = int(input())
sumS = 0
totalA = 0
for i in range(numberOfStu):
    stu = eval(input())
    res = (average(stu))
    sumS += int(res)
totalA = sumS / numberOfStu
print(totalA)
