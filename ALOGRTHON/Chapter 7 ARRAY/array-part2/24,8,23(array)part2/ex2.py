# Ex1 - String array
Text = "How are you?"

#1 - Display word by word from text
#   How
#   are
#   you?
# word = ''

for i in range(len(Text)):
    if Text[i] == ' ':
        print(word)
        word = ''
    else:
        word += Text[i]
print(word)


#2 - Create new array from text seperate by space
# ["How","are","you?"]
# arr = []
# word = ''
# for i in range(len(Text)):
#     if Text[i] == ' ':
#         arr.append(word)
#         word = ''
#     else:
#         word += Text[i]
# arr.append(word)
# print(arr)

# ---------------------------------------------------
# Ex2 - String array

# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]

#1 - How many banana in list
# count = 0
# for i in range(len(arr)):
#     if arr[i] == 'banana' or arr[i] == 'Banana':
#         count +=1
# print(count)



#2 - How many letter "o" in list
# count = 0
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(len(word)):
#         if word[j] == 'o':
#             count +=1
# print("letter 'a' in list is " +str(count))




#3 - Replace banana by Jackfruit

# for i in range(len(arr)):
#     if arr[i] == 'banana' or arr[i] == 'Banana':
#         arr[i] = 'Jackfruit'
# print(arr)


# 4 - Create new list with unique fruit
# def checkValue(value, list):
#     isique = True
#     for i in range(len(list)):
#         if value == list[i]:
#             isique = False
#     return isique
# arr = ["banana","banana","Apple","coconut", "mango", "coconut"]
# list = []
# for i in range(len(arr)):
#     if checkValue(arr[i],list):
#         list.append(arr[i])
# print(list)

# ["banana","Apple","coconut", "mango"]
#5 - Create new list store only letter "A" and "C" from list
# list = []
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(len(word)):
#         if word[j] == 'A' or word[j] == 'a' or word[j] == 'c' or word[j] == 'C':
#             list.append(word[j])
# print(list)
# -------------------------------------------------------------



# Ex3 - String array
# arr = ["banana","apple","mango", "Coconut"]
#1 - How many letter of each value
# list = []
# for i in range(len(arr)):
#     word = arr[i]
#     n = len(word)
#     list.append(n)
#     n = 0
# print(list)
#   [6,5,5,7]

#2 - How many "A" letter of each value
# list = []
# count = 0
# for i in range(len(arr)):
#     word = arr[i]
#     for j in range(len(word)):
#         if word[j] == 'A' or word[j] == 'a':
#             count +=1
#     list.append(count)
#     count = 0
# print(list)
#   [3,1,1, 0]


#3 - Move banana to last index
# word = arr[0]
# arr.pop(0)
# arr.append(word)
# print(arr)


# for i in range(len(arr)):
#     if arr[i] == 'banana':
#         word = arr[i]
#         arr.append(word)
#         arr.pop(i)
# print(arr)

#4 - Reverse each value in list
#   ['ananab','elppa'...]
list = []
store = ''
for i in range(len(arr)):
    word = arr[i]
    print(word)
    for j in range(len(word)):
        store += word[-1-j]
    list.append(store)
    store = ''
print(list)

