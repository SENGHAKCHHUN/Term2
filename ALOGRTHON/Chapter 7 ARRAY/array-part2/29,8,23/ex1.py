# Ex1 - Loop
#1 - loop to display from 10 to 1 (while)
# i = 0
# while i < 11:
#     if i > 0:
#         print(11-i)
#     i +=1



#2 - loop to display only number between 10 to 20 (while)
# i = 0
# while i < 21:
#     if i >= 10:
#         print(i)
#     i +=1



#3 - Loop to display from 50 to 40 (while)
# i = 50
# while i < 51:
#     if i > 39:
#         print(i)
#     i -=1



# Ex2 - String
# text = "125345645"
#1 - Sum all number (while)
# sum = 0
# i = 0
# while i < len(text):
#     sum += int(text[i])
#     i +=1
# print(sum)



#2 - Find first index of 5 (while)
# index = 0
# i = 0
# bool = False
# while i < len(text) and not bool:
#     if text[i] == '5':
#         index = i
#         bool = True
#     i  +=1
# print(index)



#3 - Find average all number (while)
# sum = 0
# i = 0
# average = 0
# while i < len(text):
#     sum += int(text[i])
#     i +=1
# average = sum / len(text)
# print(average)




# Ex3 - String
text = "10 12 4 11"
#1 - Sum all number seperate by space (while)
# sum = 0
# i = 0
# number = ''
# while i < len(text):
#     if text[i] != ' ':
#         number += text[i]
#     else:
#         sum += int(number)
#         number = ''
#     i +=1
# sum += int(number)
# print(sum)



#2 - find average of that number (while)
# sum  = 0
# i = 0
# number = ''
# while i < len(text):
#     if text[i] != " ":
#         number += text[i]
#     else:
#         sum += int(number)
#         number = ''
#     i +=1
# sum += int(number)
# average = sum / len(text)
# print(average)

#3 - how many number greater than 10 (while)
# count = 0
# i = 0
# number = ''
# while i < len(text):
#     if text[i] != ' ':
#          number += text[i]
#     elif text[i] == ' ' or i == len(text)-1:
#          if int(number) > 10:
#               count +=1
#     i +=1
# print(count)



# Ex4 - Array (using while loop only)
# arr = [1, 3, 5, 8, 9, 0, 5]
# #1 - find index of 9
# index = 0
# i =0
# bool = False
# while i < len(arr) and not bool:
#     if arr[i] == 9:
#         bool = True
#         index = i
#     i += 1
# print("index of 9 is index " + str(index))


#2 - find last index of 5
# i = 0
# index = 0
# while i < len(arr):
#     if arr[i] == 5:
#         index = i
#     i +=1
# print("last index of five is " + str(index))




#3 - find first index of 5
# i = 0
# index = 0
# bool = False
# while i < len(arr) and not bool:
#     if arr[i] == 5:
#         index = i
#         bool = True
#     i +=1
# print("Frsit index of 5 is " + str(index))


#4 - sum only odd number
# i = 0
# sum = 0
# while i < len(arr):
#     if arr[i] % 2 != 0:
#         sum += arr[i]
#     i +=1
# print(sum)


#5 - remove 8 from list
arr = [1, 3, 5, 8, 9, 0, 5]
# i = 0
# index = 0
# while i < len(arr):
#     if arr[i] == 8:
#         index = arr[i]
#     i +=1
# arr.remove(index)
# print(arr)



#6 - replace 0 by 33
i = 0
while i < len(arr):
    if arr[i] == 0:
        arr[i] = 33
    i +=1
print(arr)