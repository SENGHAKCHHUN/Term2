number = input()
isStop = False
i = 0
while i < len(number) and not isStop:
    if int(number[i])<6:
        isStop = True
        result = False
    else:
        result = True
    i +=1
print(result)




