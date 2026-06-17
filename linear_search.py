# Linear Search Program in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index position
    
    return -1  # element not found


# Input array
numbers = [10, 20, 30, 40, 50]

# Element to search
target = 30

# Function call
result = linear_search(numbers, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")