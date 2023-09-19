text = (input())
i = 0
result = "NOT SORTED"
isStop = False
while i < len(text)-1 and not isStop:
    if int(text[i]) < int(text[i+1]):
        result="SORTED"
        i += 2
    else:
        isStop = True
        i += 2
print(result)



