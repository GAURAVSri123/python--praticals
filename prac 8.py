# Input list using for loop
input_list = [1, 2, 3, 4, 5, 6]

cubes_of_evens = []
for num in input_list:
    if num % 2 == 0:  
        cubes_of_evens.append(num ** 3)  

print(cubes_of_evens)  



# Input list using list comprehension
input_list = [1, 2, 3, 4, 5, 6]

# List comprehension to create a list of cubes of even integers
cubes_of_evens = [num ** 3 for num in input_list if num % 2 == 0]

print(cubes_of_evens)  # Output: [8, 64, 216]
