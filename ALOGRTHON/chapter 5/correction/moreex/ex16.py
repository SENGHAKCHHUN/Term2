text = input()
res = ""
isStop = False
for i in range(len(text)):
    if i%2 == 0:
        isStop = True
    elif isStop:
        for j in range(int(text[i-1])):
            res += text[i]
        print(res)
    res = ''
    