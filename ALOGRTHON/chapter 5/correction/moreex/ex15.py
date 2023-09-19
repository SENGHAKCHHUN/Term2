number = input()
res = ""
for i in range(len(number)):
    for i in range(int(number[i])):
        res += "x"
    print(res)
    res = ""