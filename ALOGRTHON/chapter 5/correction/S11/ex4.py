text = input("text")
i = 0
result = -1
while i < len(text):
    if text[i] == "k" and text[i+1]=="k":
        result = i
        i +=2
    else:
        i +=1
print(result)
