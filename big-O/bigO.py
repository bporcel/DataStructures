# Rules about Big O
# 1. Worst Case: No matter if the required element is in the first position, we remain with O(n) and not O(1).
# 2. Remove Constants: We don't calculate for such an Specific value of Big O such as O(n + 2), we remove the constants: O(n)
# 3. Different terms for different inputs: If we have more than one element, we must use diferent terms for each one. O(n,m)
# 4. Drop non dominants: If we have a complex Big O such as O(n + n²) we drop the non dominant which is 'n'. So it remains -> O(n²).

# -------------------------------------------------------------------

def printColors(colors): 
    for color in colors: # O(n)
        print(color)

colors = ['blue', 'red', 'green', 'blue', 'yellow', 'green']
printColors(colors)

# O(n) -- Linear Time: Number of operations equals number of elements.

def printTwoColors(colors):
    print(colors[0]) # O(1)
    print(colors[1]) # O(1)

printTwoColors(colors) 

# O(2) -- Constant time: No matter the number of elements, operations remain the same.
# in this case there are 2 operations si we represent it like O(2).
# -----------------------------------------------------------------
# Specific way to calculate the Big O Notation of the whole algorithm, we must sum both Big O.

# O(n) + O(1) + O(1) = n + 1 + 1 = Big O(n + 2)

# We remove the constants (numbers which remain constant): O(n)

# ----------------------------------------------------------------

def printColorsAndAnimals(colors, animals):
    for color in colors:
        print(color)

    for animal in animals:
        print(animal)

animals = ['lion','cat','dog','lizzard']

printColorsAndAnimals(colors, animals)

# As each parameter has different lenghts, we use diferent terms for diferent inputs:
# Big O(n + m)

def logAllPairsOfAnArray(numbers):
    for number in numbers:
        print(number)

    for number in numbers:
        for n in numbers:
            print ('[',number,',',n,']')

numbers = [1,2,3,4,5]
logAllPairsOfAnArray(numbers)

# O(n²) -- Quadratic Time: If the element size increases, the operations increase quadratically: For 3 elements we make 9 operations. NOTICE NESTED LOOPS!! Might be Quadratic Time. We remove 'n' from O(n + n²) so it remains O(n²) because of rule 4. Drop non dominants.

def factorialTime(i):
    for j in range(i):
        print(j)
        factorialTime(j)

factorialTime(4)

# O(n!) -- Worst performance ever. One loop for each element.

# O(2^n) -> Exponential Time:  Recursive algorithms that solve a problem of size n
def fibonacciRecursive(index):
    if index < 2:
        return index
    return fibonacciRecursive(index - 2) + fibonacciRecursive(index - 1)

fibonacciRecursive(5)

# O(n log n) -> You loop through the full input once and then divede and conquer

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

