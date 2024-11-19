#frequency of characters
string = "I am a CS student"
char = input("enter the character: ")
n = 0
for i in string:
    if i == char:
        n +=1
    print("frequency of", char, "is:", n)
 # replace the characters   
print(string.replace("am","was"))

#replace the first occurance
print(string[1:len(string)])

#remove the all occurances
print(string[:0])
    