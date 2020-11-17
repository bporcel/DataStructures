# Given 2 sorted arrays, create one including all elements sorted
# I.E -> [0,3,4,31] & [4,6,30] => [0,3,4,4,6,30,31]


def mergeSortedArrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1


def mergeSortedArrays2(arr1, arr2):
    for item in arr1:
        arr2.append(item)

    arr2.sort()
    return arr2


def mergeSortedArrays3(arr1, arr2):
    if type(arr1) == list and type(arr2) == list:
        array = []
        for item in arr1:
            array.append(item)
        for item in arr2:
            array.append(item)

        array.sort()
        return array
    return 'Input was not an array'

def mergeSortedArrays4(arr1, arr2):
    arr1First = arr1[0]
    arr2First = arr2[0]
    array = []
    while True:
        if arr1First < arr2First:
            array.append(arr1First)
            arr1First = arr1[1]
            del arr1[0]
        elif arr2First < arr1First:
            array.append(arr2First)
            arr2First = arr2[1]
            del arr2[0]
        else:
            array.append(arr1First)
            array.append(arr2First)
            arr1First = arr1[1]
            arr2First = arr2[1]
            del arr1[0]
            del arr2[0]


print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))
print(mergeSortedArrays([], [4, 6, 30]))
print(mergeSortedArrays2([0, 3, 4, 31], [4, 6, 30]))
print(mergeSortedArrays2([0, 3, 4, 31], []))
print(mergeSortedArrays3([0, 3, 4, 31], [4, 6, 30]))
print(mergeSortedArrays3([], [4, 6, 30]))
print(mergeSortedArrays4([0, 3, 4, 31], [4, 6, 30]))
