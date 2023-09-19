text = input()
sum = ""
result = ""
isStop = False
i =0
while i < len(text)-1 and not isStop:
    if text[i] == 'a' and text[i+1] == 'b':
        result = "YES"
        i += 2
    else:
        result = "NO"
        isStop = True
print(result)

