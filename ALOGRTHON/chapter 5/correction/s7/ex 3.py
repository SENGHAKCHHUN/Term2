text = input()
sum = 0
i = 0
while i<len(text)-1:
    if text[i] == 'a' and text[i+1]=='b':
        sum +=1
    i+=2
print(sum)

