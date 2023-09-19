text = input()
result = True
i = 0
isSeven = False
while i < len(text)-1 and not isSeven:
    if text[i] == 'a' or text[i] == 'A':
        result = "True"
    else:
        result = "False"
        isSeven = True
    i+=1
print(result)