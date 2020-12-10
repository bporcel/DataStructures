# Pretty much best time complexity in all cases O(n log n)
# But takes a larger Space complexity O(n)
def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers

    # Split array in left and right
    fullLen = len(numbers)
    halfLen = int(len(numbers) / 2)
    left = numbers[0:halfLen]
    right = numbers[halfLen:fullLen]
    print('left -> ', left)
    print('right -> ', right)

    return merge(
        mergeSort(left),
        mergeSort(right)
    )


def merge(left, right):
    sortedArray = []
    i = 0
    j = 0
    while i < len(left):
        while j < len(right):
            if right[j] < left[i]:
                sortedArray.append(right[j])
                del right[j]
            else:
                sortedArray.append(left[i])
                del left[i]
                i -= 1
                break
        i += 1
    if len(right) > 0:
        sortedArray.extend(right)
    elif len(left) > 0:
        sortedArray.extend(left)
    return sortedArray


numbers = [2, 6, 78, 8, -7, 1, 0]
print(mergeSort(numbers))
