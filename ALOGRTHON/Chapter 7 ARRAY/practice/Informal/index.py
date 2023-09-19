# arr = ['0','0','*','0','0','0','0']
def findIndex(arr):
    index = None
    for i in range(len(arr)):
        if arr[i] == '*':
            index = i
    return index
arr = ['0','0','*','0','0','0','0']
Run = True
while Run:
    currentPosition = findIndex(arr)
    command = input('enter ')
    if command.lower() == 'l' and currentPosition > 0:
        arr[currentPosition] = '0'
        arr[currentPosition-1] = '*'
        print(arr)
    elif command.lower() == 'r' and currentPosition < len(arr)-1:
        arr[currentPosition] = '0'
        arr[currentPosition+1] = '*'
        print(arr)
    elif currentPosition == 0:
        print('please go right')
    elif currentPosition == len(arr) -1:
        print('please go left')
    else:
        if command == 'stop':
            Run = False
            print('Finish Action')
        else:
            print('unknow' + command + 'command')
    
