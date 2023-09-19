# Ex4 - Array 2D
arr2D = [
  ['*','0','0'],
  ['*','0','0'],
  ['*','0','0']
]
i = 0
bool = True
Run = True
while i < len(arr2D) and Run:
  j = 0
  while j < len(arr2D[i]) and bool:
    if arr2D[j][i] != '*':
      bool = False
    j +=1
  i +=1
  if bool:
    print('win')
    Run = False
if not bool:
  print('lost')
# 1 - ouput: Win




arr2D = [
  ['*','*','*'],
  ['0','0','0'],
  ['0','0','0'],
]
i = 0
bool = True
Run = True
while i < len(arr2D) and Run:
  j = 0
  while j < len(arr2D[i]) and bool:
    if arr2D[i][j] != '*':
      bool = False
    j +=1
  i +=1
  if bool:
    print('win')
    Run = False
if not bool:
  print('lost')
#2 - ouput: Win




arr2D = [
  ['*','0','0'],
  ['0','*','0'],
  ['0','0','*'],
]
i = 0
bool = True
Run = True
while i < len(arr2D) and Run:
  j = 0
  while j < len(arr2D[i]) and bool:
    if arr2D[i][j] != '*':
      bool = False
    j +=1
  i +=1
  if bool:
    print('win')
    Run = False
if not bool:
  print('lost')
#3 - ouput: lost



arr2D = [
  ['*','*','0'],
  ['0','0','0'],
  ['0','0','*'],
]
i = 0
bool = True
Run = True
while i < len(arr2D) and Run:
  j = 0
  while j < len(arr2D[i]) and bool:
    if arr2D[i][j] != '*':
      bool = False
    j +=1
  i +=1
  if bool:
    print('win')
    Run = False
if not bool:
  print('lost')
#4 - ouput: Lose
