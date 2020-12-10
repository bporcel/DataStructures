def binarySearch(numbers, item):
    tmp = sorted(numbers)
    halfLen = int(len(tmp) / 2)
    fullLen = len(tmp)
    found = False
    while not found and len(tmp) > 0:
        if tmp[halfLen -1] > item:
            tmp = tmp[0:halfLen]
            halfLen = int(len(tmp) / 2) 
        elif tmp[halfLen -1] < item:
            tmp = tmp[halfLen: fullLen]
            halfLen = int(len(tmp) / 2) 
        else:
            found = True
    return found

numbers = [1, 3, 6, 4, 0, 5]
print(binarySearch(numbers, 0))