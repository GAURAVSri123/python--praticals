char = input("Enter the value:")

if char >='A' and char<='z':
    print("uppercase letter")

elif char>="a" and char<="z":
    print("lowercase letter")

elif char>='0' and char<='9':
    print("Numeric digit")
    n= int(char)

    dict = {0:'zero' , 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

    print(dict[n])
else:
    print("special character")



    
