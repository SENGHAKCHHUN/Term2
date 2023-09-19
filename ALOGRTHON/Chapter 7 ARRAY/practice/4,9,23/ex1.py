def sumNumber(value):
    sum = 0
    for i in range(len(Numarr)):
        sum += Numarr[i]
    return sum
numerOfArr= int(input())
res = ''
total = ''
for i in range(numerOfArr):
    Numarr = eval(input())
    res = sumNumber(Numarr)
    total += str(res) + "\n"
print(total)


# Ex1:
# number of array: 3
# > [3, 3]
# > [1, 3, 4]
# > [4, 5, 9, 1]

# output:
# 6
# 8
# 19
# ———————————————-

