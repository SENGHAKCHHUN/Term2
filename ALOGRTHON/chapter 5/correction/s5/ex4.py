text = input()
result=""
isSeven = False
i = 0
while i < len(text)-1 and not isSeven:
    if text[i] > text[i+1]:
        result = "NOT SORTED"
        i += 1
        isSeven = True
    else:
        result = "SORTED"
        i += 1
print(result)
