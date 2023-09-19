# def CountNumberOfA(array):
#     count = 0
#     total = ""
#     for i in range(len(array)):
#         word = array[i]
#         for j in range(len(word)):
#             if word[j] == 'a' or word[j] == 'A':
#                 count +=1
#         total += "Number of A in " + array[i] + " is " + str(count) +"\n"
#     return total
# array = eval(input())
# print(CountNumberOfA(array))

# list = eval(input())
# for i in range(len(list)):
#     print(list[i])

# list = ["chal","yon","Ya","yiem","chan","senghak","maly"]
# for i in range(len(list)):
#     print(list[i])


# list = ["maly", "chal", "yon", "Ya", "yiem", "chan", "senghak"]
# count = 0
# res = ""
# for i in range(len(list)):
#     text = list[i]
#     for j in range(len(text)):
#         if text[j] == 'A' or text[j] == 'a':
#             count += 1
#     res += "Mumber of A in "+ list[i] + " is " + str(count)+"\n"
# print(res)


# Enter your code here. Read input from STDIN. Print output to STDOUT
array = eval(input())
word = ""
bool = False
res = []
total = []

list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(array)):
    word = array[i]
    for k in range(len(word)):
        find = word[k]
        l = 0
        while l < (len(list)) and not bool:
            if find == list[l]:
                res.append(find)
            l +=1
res.sort()
i =0
while i < len(res):
    if res[i-1] != res[i]:
        total.append(res[i])
    i+=1
print(total)






