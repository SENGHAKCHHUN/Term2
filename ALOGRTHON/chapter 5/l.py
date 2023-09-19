text = input()
isStop = False
firstLetter = text[0]
for i in range(len(text)):
    if firstLetter != text[i] and not isStop:
        isStop = True
if not isStop:
    print("Yes")
else:
    print("No")
