text = input()
result = ""
isStop = False
isSeven = False
isFound = False
i = 0
while i < len(text) and not isStop:
    if text[i] == "x" and not isSeven:
        result = "Ok"
    elif text[i] != "x" and not isSeven:
        isStop = True
        result = "WRONG"
    elif text[i] == "[":
        isSeven = True
    elif text[i] == "y" and not isFound:
        result = "Ok"
    elif text[i] != "y":
        isStop = True
    elif text[i] == "]":
        isFound = True
    elif text[i] == "x":
        result == "Ok"
    elif text[i] != "x":
        result = "WRONG"
    i +=1
print(result)
        





