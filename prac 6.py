string1 ="Hello python"
string2 = "I am doing code in python"
n1= int(input("enter the no to be swap: "))

p = string1[:n1]
q = string2[n1:]

if n1<= min(len(string1),len(string2)):
    print(string1.replace(p,q))

else:
    print(string2.replace(q,p))
    
