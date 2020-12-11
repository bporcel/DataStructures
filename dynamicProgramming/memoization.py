def addTo80(n):
    return 80 + n

def memoizedAddTo80(n):
    if n in cache:
        return cache[n]
    else:
        print('Long time calculation')
        cache[n] = 80 + 5
        return cache[n]

cache = {}

print('Memo cutre 1 ->', memoizedAddTo80(5))
print('Memo cutre 2 ->', memoizedAddTo80(5))

# ------------------------------------

def memoizedAddTo80ProStyle():
    cache = {}

    def addTo80(n):
        if n in cache:
            return cache[n]
        else:
            print('Long time calculation')
            cache[n] = 80 + n
            return cache[n]
    return addTo80
memoized = memoizedAddTo80ProStyle()
print('Memo pro 1 -> ', memoized(5))
print('Memo pro 2 -> ', memoized(5))
