# -------------------------------
# Ex4 Array 2D
# arr = [
#   ['banana', 'mango', 'mango', 'Jackfruit'],
#   ['orange', 'coconut', 'banana', 'papaya'],
#   ['apple', 'orange', 'mango', 'coconut'],
#   ['mango', 'coconut', 'banana', 'papaya'],
#   ['banana', 'apple', 'orange', 'coconut'],
# ]
#1 - How many fruit in list
def count_fruit(arr):
    res = 0
    for family in range(len(arr)):
        res += len(arr[family])
    return res
arr = [
  ['banana', 'mango', 'mango', 'Jackfruit'],
  ['orange', 'coconut', 'banana', 'papaya'],
  ['apple', 'orange', 'mango', 'coconut'],
  ['mango', 'coconut', 'banana', 'papaya'],
  ['banana', 'apple', 'orange', 'coconut'],
]
print('There are ' + str(count_fruit(arr)) + ' fruit in list')
            

#2 - How many mango, orange, banana, coconut
def count_fruit(arr,value):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == value:
                count += 1
    return count
arr = [
  ['banana', 'mango', 'mango', 'Jackfruit'],
  ['orange', 'coconut', 'banana', 'papaya'],
  ['apple', 'orange', 'mango', 'coconut'],
  ['mango', 'coconut', 'banana', 'papaya'],
  ['banana', 'apple', 'orange', 'coconut'],
]
print("Mumbers of mango is "+str(count_fruit(arr,"mango")))
print("Mumbers of orange is "+str(count_fruit(arr,"orange")))
print("Mumbers of banana is "+str(count_fruit(arr,"banana")))
print("Mumbers of coconut is "+str(count_fruit(arr,"coconut")))


#3 - How many letter "o" in list
def count_letter(list):
    count = 0
    for i in range(len(list)):
        for h in range(len(list[i])):
            if list[i][h] == 'o':
                count +=1
    return count
arr = [
  ['banana', 'mango', 'mango', 'Jackfruit'],
  ['orange', 'coconut', 'banana', 'papaya'],
  ['apple', 'orange', 'mango', 'coconut'],
  ['mango', 'coconut', 'banana', 'papaya'],
  ['banana', 'apple', 'orange', 'coconut'],
]
count = 0
for j in range(len(arr)):
    count += count_letter(arr[j])
print('Letter o in array is ' + str(count))


#4 - How many fruits has 6 character
def count_letter(list):
    numberOfletter = 0
    count = 0
    for i in range(len(list)):
        numberOfletter = len(list[i])
        if numberOfletter == 6:
            count += 1
    return count
arr = [
  ['banana', 'mango', 'mango', 'Jackfruit'],
  ['orange', 'coconut', 'banana', 'papaya'],
  ['apple', 'orange', 'mango', 'coconut'],
  ['mango', 'coconut', 'banana', 'papaya'],
  ['banana', 'apple', 'orange', 'coconut'],
]
count = 0
for j in range(len(arr)):
    count += count_letter(arr[j])
print('Fruits has 6 chararter is '+ str(count))