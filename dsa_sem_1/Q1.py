# Create a list (array) of numbers
# numbers = [15, 8, 42, 23, 4, 99, 16]


# min_val = min(numbers)
# max_val = max(numbers)

# print("Array:", numbers)
# print("Minimum value:", min_val)
# print("Maximum value:", max_val)

#find 2nd min and max
numbers = [15, 8, 42, 23, 4, 99, 16]
nums = sorted(set(numbers))

print("Second Minimum:", nums[1])
print("Second Maximum:", nums[-2])