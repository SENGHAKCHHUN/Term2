def replaceNumber(number):
    if len(number)!=0:
        res =""
        for i in range(len(number)):
            if int(number[i]) == 9:
                res += '168'+","
            else:
                res += str(number[i])+","
        return res
    return []
n = eval(input())
print(replaceNumber(n))
