text = input()
i = 0
result = 0
isStop = False
while i < len(text) and not isStop:
    if text[i] == 'o' or text[i] == 'O':
        result = i
        isStop = True
    i += 1
if isStop:
    print(result)
else:
      print("-1")







