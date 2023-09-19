res = ""
isSix = False
for i in range(5):
    number = int(input())
    if number >= 10 and number<=30 and not isSix:
        res = "WIN"
    else:
        isSix = True
        res = "LOST"
print(res)