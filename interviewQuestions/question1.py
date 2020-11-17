# Given 2 arrays, create a function that let the user know (true/false) whether these 2 arrays contain any common items.
# Example 1:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# return False

# Example 2:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']
# return True

def findEquals(array1, array2):
    for c in array2:
        if c in array1:
            return True
    return False


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
print(findEquals(array1, array2))
