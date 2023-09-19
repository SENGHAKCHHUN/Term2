number = input()
res = ""
even = ""
add = ""
for i in range(len(number)):
    if number[i].isnumeric():
        res += number[i]
    else:
        if int(res)%2 == 1:
            add += res + " "
        elif int(res)%2 == 0:
            even += res + " "
        res = ""
if int(res)%2 == 1:
    add += res
else:
    even += res 
print("even" + str(even))
print("add" + str(add))



# number = input()
# res = ""
# for i in range(len(number)):
#     if int(number[i])%2 == 1:
#         res += number[i]
# print(res)

