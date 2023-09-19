number = int(input("number"))
sum = 0
result = ""
for i in range(number):
    sum = number - i
    result += str(sum) + " "
print(result)