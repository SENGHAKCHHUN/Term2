def capitalize(string):
    res = ""
    isFalse = False
    for i in range(len(string)):
        if string[0].islower() and not isFalse:
            res += string[i].upper()
            isFalse = True
        elif string[i].islower() and i < len(string)-1:
            res+=string[i]
        elif i < len(string):
            res+=string[i].upper()
    return res
text = input()
print(capitalize(text))


        
    