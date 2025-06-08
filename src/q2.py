    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return None  # You could also raise an error or return an empty list
    
    # Replace each element if it matches find_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
            
    return lst
    
    # Test 1
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
# Output: [1, 5, 3, 4, 5, 5]

# Test 2
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
# Output: ['orange', 'banana', 'orange']
