

#    Ex2
# 1 - Get value from input as a string

string = input()

# 2 - display one letter by one letter using for loop

# for i in range(len(string)):
#     print(string[i])

# 3 - check if in string contains single quote ' ' open and close

isFalse = False
result = ""
for i in range(len(string)):
    if string[i] == "'":
        i = 0
        while i+1 < len(string) and not isFalse:
            

print(result)
# 4 - get only letter inside single quote ' '
# 5 - get only letter outside single quote ' '
 

    