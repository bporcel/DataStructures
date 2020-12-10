# Really fast if data is almost sorted or its a small input
def insertionSort(numbers):
    numbersSize = len(numbers)
    for i in range(1, numbersSize):
        if numbers[i] < numbers[0]:
            tmp = numbers[i]
            del numbers[i]
            numbers.insert(0, tmp)
        else:
            aux = i
            for j in range(i - 1, 0, -1):
                if numbers[aux] < numbers[j]:
                    tmp = numbers[aux]
                    del numbers[aux]
                    numbers.insert(j, tmp)
                    aux = j

numbers = [2, 65, 34, 2, 1, 7, 8]
insertionSort(numbers)
print(numbers)
