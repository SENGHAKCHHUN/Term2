number = input()
res = ""
isBig = 0
for i in range(len(number)):
    if number[i].isnumeric():
        res+= number[i]
    else:
        if int(res) > int(isBig):
            isBig = res
        res = ""
if int(res) > int(isBig):
    isBig = res
print(isBig)

