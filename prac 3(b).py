#print a reverse pyramid
n = 5
for i in range(n,0,-1):
    print("*"*(2*i-1)," "*(n-i))