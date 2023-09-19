# ------------------------------
# Ex5 - Array 2D
# arr = [
#   [0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 2]
#   [0, 0, 0, 0, 2],
#   [0, 0, 0, 1, 1]
# ]
#1 - How many 1 number in list
def countNumber(arr):
  count = 0
  for i in range(len(arr)):
    if arr[i] == 1:
      count += 1
  return count
arr = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1, 1]
]
res = 0
for i in range(len(arr)):
  res += countNumber(arr[i])
print('Number one in array is '+str(res))
    

#2 - Replace 0 with $
def replace_number(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] == 0:
        arr[i][j] = '$'
  return arr
arr = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1, 1]
]
print(replace_number(arr))


#3 - Replace 1 with 0 and replace 0 with 1
def replace_number(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] == 0:
        arr[i][j] = 1
      elif arr[i][j] == 1:
        arr[i][j] = 0
  return arr
arr = [
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1, 1]
]
print(replace_number(arr))