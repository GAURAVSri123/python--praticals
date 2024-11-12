# Input the number n
n = int(input("Enter a number: "))

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate and print all prime numbers till n
print(f"Prime numbers up to {n}:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")

# generatre the first prime n numbers
count = 0
num =2

print(n,"first prime numbers")
while count<n:
    if is_prime(num):
        print(num,end=" ")

        count+= 1
        num+= 1
