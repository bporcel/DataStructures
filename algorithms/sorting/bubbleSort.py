def bubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) -1):
            pointer = numbers[j]
            nextPointer = numbers[j+1]
            if pointer > nextPointer:
                numbers[j] = nextPointer
                numbers[j+1] = pointer

numbers = [2, 65, 34, 2, 1, 7, 8]
bubbleSort(numbers)
print(numbers)