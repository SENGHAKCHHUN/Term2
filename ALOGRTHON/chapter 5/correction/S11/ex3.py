result = ""
i = 0
isStop = False
isFalse = False
while i != 'end' and not isStop:
    number = input()
    if number != "end":
        if int(number)%2 == 0 and not isFalse:
            result +=number  
            isFalse = True
        elif int(number)%2 == 0 and isFalse:
            result += ":" + number
    elif number == "end":
        isStop = True
    i +=1
print(result)