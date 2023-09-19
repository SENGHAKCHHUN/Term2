text = input()
res = ""
for i in range(len(text)):
    if text[i] == 'a' or text[i] == 'A':
        res += "*"
    elif text[i] == 'b' or text[i] == 'B':
        res += "$"
    else:
        res += text[i]
print(res)