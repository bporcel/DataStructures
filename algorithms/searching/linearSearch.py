def linearSearch(numbers, item):
    for n in numbers:
        if n == item:
            return True
    return False
    
def linearSearch2(numbers, item):
    return True if item in numbers else False

def linearSearch3(numbers, item):
    return True if numbers.index(item) else False

numbers = [1, 3, 6, 4, 0, 5]
print(linearSearch(numbers, 6))
print(linearSearch2(numbers, 6))
print(linearSearch3(numbers, 6))
