word1 = input()
word2 = input()
number = 0
for i in range(len(word1)):
    if word1[i].isupper():
        number += 1
for i in range(len(word2)):
    if word2[i].isupper():
        number +=1
print(number)