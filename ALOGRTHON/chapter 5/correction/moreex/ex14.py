text = input()
res = ""
negativeNumber = ""
for i in range(len(text)):
    if text[i] != " " or text[i] == "-":
        res += text[i]
    elif text[i] == " ":
        if int(res) < 0:
            negativeNumber += res +","
        res = ''
if int(res) < 0:
    negativeNumber += res 
print(negativeNumber)

