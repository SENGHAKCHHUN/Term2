import os
choice = input("good bye or stay here(y / n)")
if choice.lower() == 'y':
    os.system("shutdown /s")
else:
    print("edit the program")