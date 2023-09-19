def sumFromTo(array):
    if len(array) == 2:
        if int(array[0]) < int(array[1]):
            sum = 0
            i = 0
            num1 = int(array[0])
            num2 = int(array[1])
            while num1 < num2+1:
                sum += num1
                num1+=1
                i +=1
            res = sum
        else:
            res = 0
    else:
        res = "You got Error"
    return res
num1 = eval(input())
print(sumFromTo(num1))

 



