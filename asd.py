string = dict(((i[0], i[1]) for i in list(enumerate("9;01asorActoRactoaaa".lower())))) # input("Enter string: ") 
                                                            #^^^^^
user_string = "actor".lower() # input("Enter string what you whant to find in 1-st string: ")


# Solving with Strings
# string = "acT;ocltAActorfty".lower()

# len_user_str = len(user_string)
# for i in range(len(string)-len_user_str+1):
#     if user_string == string[i:len_user_str+i]:
#         print(i)


i = 0
count = 0
for j in string:
    if user_string[i] == string.get(j):
        count += 1
    elif user_string[0] == string.get(j):
        i = 0
        count = 1
    else:
        i = 0
        count = 0
    
        
    if count == len(user_string):
        print(j-len(user_string)+1)
        exit()
    i += 1
    if i > len(user_string)-1:
        i = 0
        count = 0

print("String not found")
print(string)