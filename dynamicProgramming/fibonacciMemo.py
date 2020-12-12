# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...

def memoFib():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                return cache[n]
    return fibonacci

memonacci = memoFib()
print(memonacci(80))
