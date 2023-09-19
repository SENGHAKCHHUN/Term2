number = input()
sum = 0
res = ""
for i in range(len(number)):
    if number[i]!= " ":
        res += number[i]
    else:
        if number[i] == " ":
            sum += int(res)
        res = ""
sum += int(res)
if sum <= 20:
    print("WON")
else:
    print("LOST")