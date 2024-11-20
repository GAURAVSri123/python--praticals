# find the occurrances in main_string into sub_string
def find_all_occurrences(main_string, sub_string):
    # List to store indices of occurrences
    indices = []
    # Starting
    start = 0

    while True:
        # Find the next occurrence of sub_string in main_string
        idx = main_string.find(sub_string, start)
        if idx == -1:
            break 
        indices.append(idx)  
        start = idx + 1  

    return indices if indices else -1

main_string = "Hello python"
sub_string = "python"
result = find_all_occurrences(main_string, sub_string)
print(result) 
