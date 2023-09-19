# Ex5 - Array
# Keep only word with at least 1 letter A
# input: banana coconut mango jackfruit
# ouput:
# banana mango jackfruit
text = input()
word = ''
res = ''
for i in range(len(text)):
    bool = False
    if text[i] != ' ' and len(text)-1 != i:
        word += text[i]
    elif text[i] == ' ' or len(text)-1 == i:
        if len(text)-1 == i:
            word += text[i]
        j = 0
        while j < len(word) and not bool:
            if word[j].lower() == 'a':
                res += word + ' '
                bool = True
            j +=1
        word = ''
print(res)


        



