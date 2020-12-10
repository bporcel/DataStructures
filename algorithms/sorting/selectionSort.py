# Normally used for educational purpouses
def selectionSort(numbers):
    for i in range(len(numbers)):
        smallest = numbers[i]
        tmp = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < smallest:
                smallest = numbers[j]
                tmp = j
        numbers[tmp] = numbers[i]
        numbers[i] = smallest


numbers = [2, 65, 34, 2, 1, 7, 8]
selectionSort(numbers)
print(numbers)
