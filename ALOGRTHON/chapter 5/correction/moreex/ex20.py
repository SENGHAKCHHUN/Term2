text = input()
res= ""
isStop = False
for i in range(len(text)):
    if text[0].islower() and not isStop:
        res += text[0].upper()
        isStop = True
    elif text[i-1] == " ":
        res += text[i].upper()
    else: 
        res += text[i]
print(res) 


