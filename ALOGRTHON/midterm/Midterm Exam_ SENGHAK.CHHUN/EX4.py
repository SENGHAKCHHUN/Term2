i = 0
isStop = False
while i < 3 and not isStop:
    number = int(input())
    if number == 68:
        print("YOU WON")
        isStop = True
    elif i == 0 or i ==1 and number != 68:
        print("ENTER NUMBER AGAIN")
    else:
        print("YOU LOST")
    i +=1

 

    