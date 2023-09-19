def LetterNumber(string):
    res = "False"
    isSix = False
    for i in range(len(string)):
        if string[i].isnumeric():
            isSix = True
        elif isSix:
            res = "True"
        else:
            isSix = True
    return res
text = input()
print(LetterNumber(text))