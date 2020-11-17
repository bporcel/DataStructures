strings = ['a', 'b', 'c', 'd']
# En un sistema de 8 bits, utilizariamos 4 Bytes por cada elemento del array.
# 4*4 = 16 Bytes

# Access O(1)
print(strings[2]) 

# Push at the end O(1). Might be O(n) if the system realocates the data to add the new element.
strings.append('e')
print(strings)

# Remove las item O(1)
strings.pop() 
print(strings)

# Insert at the beginning of the list O(n). Because we have to move all the items one position
strings.insert(0, 'z')
print(strings)
