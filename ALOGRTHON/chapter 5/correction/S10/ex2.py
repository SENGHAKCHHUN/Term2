number = input()
Multiple = 1
isStop = False
for i in range(len(number)):
    if number[i] !="6" and not isStop:
        Multiple *= int(number[i])
    else:
        isStop = True
print(Multiple)