# -------------------------------
# Ex3 - Array 2D
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
#1 - How many number 2 in list
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            count +=1
print("Number 2 is " + str(count))


#2 - Sum only number > 5
def sumNumber(arr):
    sum = 0
    for rean in range(len(arr)):
        for life in range(len(arr[rean])):
            if arr[rean][life] > 5:
                sum += arr[rean][life]
    return sum
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
print(sumNumber(arr))


#3 - How many number < 5
def count_number(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] < 5:
            count +=1
    return count
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
total = 0
res = 0
for j in range(len(arr)):
    res = count_number(arr[j])
    total += res
print(total)


#4 - Sum number in row
def sumNumberRow(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
newList = []
for j in range(len(arr)):
    newList.append(sumNumberRow(arr[j]))
print(newList)


#5 - Sum number in column
def sumNumbercolumn(list):
    newList = []
    row = len(list)
    coloum = len(list[0])
    for j in range(coloum):
        sum = 0
        for i in range(row):
            sum += list[i][j]
        newList.append(sum)
    return newList
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
print(sumNumbercolumn(arr))


#6 - Replace number 8 with *
def replace_number(arr):
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] == 8:
                arr[j][i] = '*'
    return arr
arr = [
  [1, 2, 3],
  [2, 3, 4],
  [5, 6, 8],
  [10, 3, 8]
]
print(replace_number(arr))