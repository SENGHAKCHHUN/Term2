text = input()
isRun = False
res = ""
for i in range(len(text)):
    if text[i] == '#':
        isRun = True
    elif isRun:
        for j in range(4):
            res += text[i]
    else:
        res += text[i]
if len(res) > 0:
    print(res)
else:
    print("No letter")
