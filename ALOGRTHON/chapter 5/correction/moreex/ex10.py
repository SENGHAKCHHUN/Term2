text = input()
result = 0
isBig = int(text[0])
for i in range(len(text)):
    if int(text[i]) > int(isBig):
        isBig = text[i]
print(isBig)