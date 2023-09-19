number = input()
sum = 0
res = ""
for i in range(len(number)):
    if number[i] != " ":
        res += number[i]
    else:
        if number[i] == " ":
            if res != '12' and res != '10':
                sum += int(res)
            res = ""
if res != '12' and res != '10':
    sum += int(res)
if sum == 20:
    print("WON")
else:
    print("LOST")
    