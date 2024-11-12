# Find the root of a quadratic equation
a = int(input("enter value a:"))
b = int(input("enter value b:"))
c = int(input("enter value c:"))

# dicrimnant calculation
d = b**2 - 4*a*c

# roots formula

root1 = (-b + d**0.5)/ 2*a
root2 = (-b - d**0.5)/ 2*a

if d>=0:
     print("the root is real", root1,root2)
else:
     print("root is not real", root1,root2)

 