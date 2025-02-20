def max_difference(arr):
    min_element = arr[0]
    max_diff = float('-inf')

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_element)
        min_element = min(min_element, arr[i])

    return max_diff

# Example usage 
arr = [2, 3, 10, 6, 4, 8, 1]
print(max_difference(arr)) # Output: 8 (10 - 2)
