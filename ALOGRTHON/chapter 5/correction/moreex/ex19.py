number = input()
even= ""
odd = ""
for i in range(len(number)):
    if int(number[i])%2 == 0:
        even += number[i]
    else:
        odd +=number[i]
print(odd+even)