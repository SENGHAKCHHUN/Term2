# def findVowel(string):
#     res = ""
#     i=0
#     for i in range(len(string)):
#         if string[i] != 'A' or string[i]!='E' or string[i] != 'I' or string[i]!='O' or string[i] != 'U':
#             res = "Not Accepted"
#         else:
#             res ="Accepted"
#     return res
# text = input("Enter text")
# print(findVowel(text))

# Python program for the above approach
def check(string):
	if len(set(string.lower()).intersection("aeiou")) >= 5:
		return ('accepted')
	else:
		return ("not accepted")


# Driver code
if __name__ == "__main__":
    string = "abcefghijklosu"
	print(check(string))
