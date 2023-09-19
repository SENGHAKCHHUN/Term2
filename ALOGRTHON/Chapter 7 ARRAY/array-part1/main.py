def countNegNum(number):
    count = 0
    for i in range(len(number)):
        if int(number[i])<0:
            count +=1
    if count>0:
        return count
    else:
        return -1
n = eval(input())
print(countNegNum(n))    