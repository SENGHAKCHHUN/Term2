text = input()
count = 0
i = 0
while i < len(text) -1 :
    if text[i] == "a" and text[i+1] =="b" and text[i+2] =="c":
        count +=1
        i += 3
    else:
        i+=1
print(count)

