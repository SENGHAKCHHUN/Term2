def removeMinuses(String):
    res = ""
    for i in range(len(String)):
        if String[i] != '-':
            res += String[i]
    return res
isGoon = True
while isGoon:
    text = input("Enter a word")
    print("Word without minus:" + removeMinuses(text))
    letter = input("Do you want to Continue")
    if letter.upper() != 'Y':
        isGoon = False



