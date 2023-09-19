# Ex9
# From list of array 2D
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
#1 - How many letter "A" from array 2D (function)
def letterA(word):
    count = 0
    for i in range(len(word)):
        if word[i] == 'a':
            count +=1
    return count
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
res = ''
total = 0
for i in range(len(fruits)):
    res = fruits[i]
    for j in range(len(res)):
        word = res[j]
        count = letterA(word)
        total += count
print('letter from array 2D is ' + str(total))

#2 - How many banana in list (function)
def NumberofBanana(array):
    count =0
    for j in range(len(array)):
        if array[j] == 'banana':
            count +=1
    return count
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
total = 0
res = 0
for i in range(len(fruits)):
    res = NumberofBanana(fruits[i])
    total += res
print(total)


#3 - How many mango in list (function)
# def NumberofBanana(array):
#     count =0
#     sen = ''
#     for i in range(len(array)):
#         sen = array[i]
#         for j in range(len(sen)):
#             if sen[j] == 'mango' or sen[j] == 'Mango':
#                 count +=1
#     return count
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
# print(NumberofBanana(fruits))



#4 - How many orange in list (function)
# def NumberofBanana(array):
#     count =0
#     sen = ''
#     for i in range(len(array)):
#         sen = array[i]
#         for j in range(len(sen)):
#             if sen[j] == 'orange':
#                 count +=1
#     return count
# fruits = [
#   ['banana','coconut','mango'],
#   ['jackfruit','banana','mango'],
#   ['papaya','apple','orange'],
#   ['mango','orange','Mango'],
#   ['banana','mango','orange']
# ]
# print(NumberofBanana(fruits))


#5 - Replace mango by # sign (function)
def NumberofBanana(array):
    sen = ''
    for i in range(len(array)):
        sen = array[i]
        for j in range(len(sen)):
            if sen[j] == 'mango' or sen[j] == 'Mango':
                sen[j] = "#"
    return fruits
fruits = [
  ['banana','coconut','mango'],
  ['jackfruit','banana','mango'],
  ['papaya','apple','orange'],
  ['mango','orange','Mango'],
  ['banana','mango','orange']
]
print(NumberofBanana(fruits))