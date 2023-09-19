def removeNumber(text):
    res = ""
    isTrue = False
    for i in range(len(text)):
        if text[i].isnumeric():
            isTrue = True
        else:
            res += text[i]
    return res
word = input("enter word")
print(removeNumber(word))