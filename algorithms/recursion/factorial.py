# Find the factorial of a number recursively and iteratively

def iterative(n):
    result = n
    for i in range(n -1, 0, -1):
        result *= i
    return result

def recursive(n):
    if n == 1:
        return 1
    return n * recursive(n-1)

print('Iterative -> ', iterative(5))
print('Reursive -> ', recursive(5))