number = int(input())
mode = input()
if mode == "inside":
    if number >= 1 and number <= 10:
        print("True")
    else:
        print("False")
if mode == "outside":
    if number < 1 or number > 10:
        print("True")
    else:
        print("False")



