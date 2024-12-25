my_string = input().strip()

# 
max_count = 1
curr_count = 1

# Start from second character (index 1)
# Compare with previous character
for i in range(1, len(my_string)):
    if my_string[i] == my_string[i-1]:
        curr_count += 1
    else:
        curr_count = 1
    max_count = max(max_count, curr_count)


print(max_count)


# Time Complexity: O(n)
# Space Complexity: O(n)