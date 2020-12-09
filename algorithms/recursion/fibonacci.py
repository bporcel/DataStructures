# Find the fibonacci number corresponding the given index
# Fibonaci: 0, 1, 1, 2, 3, 5, 8, 13
# Ex: index: 4 -> 3

def fibonacciIterative(index):
    fibonacci = [0, 1]
    for i in range(1, index):
        number = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(number)
    return fibonacci[index]


def fibonacciRecursive(index): # BIG-O -> Exponential Time: O(2^n)
    if index < 2:              # Recursive algorithms that solve a problem of size n
        return index
    return fibonacciRecursive(index - 2) + fibonacciRecursive(index - 1)


print('Iterative -> ', fibonacciIterative(5))
print('Reursive -> ', fibonacciRecursive(4))