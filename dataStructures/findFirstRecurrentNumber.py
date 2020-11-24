# Given an array find the first recurrent number
# Ex: Input -> [2,5,1,2,3,3]
# Must return 2
#Ex2: Input [1,2,3,4]
# Must return undefined

def returnFirstRecurrent(array):
    seen = {}
    if type(array) is list:
        for number in array:
            if seen.get(number):
                return number
            else:
                seen[number] = True
    return None
    
def returnFirstRecurrent2(array):
    seen = {}
    if type(array) is list:
        for number in array:
            seen[number] = True

        for number in array:
            if seen[number]:
                return number
    
    return None


# print(returnFirstRecurrent([2, 5, 1, 2, 3]))
print(returnFirstRecurrent([2, 5, 5, 2, 3]))
print(returnFirstRecurrent2([2, 5, 5, 2, 3]))
# print(returnFirstRecurrent([1, 2, 3, 4]))
# print(returnFirstRecurrent([1, 2, 'a', 'a']))
# print(returnFirstRecurrent([1,1]))
# print(returnFirstRecurrent([1]))
# print(returnFirstRecurrent([]))
# print(returnFirstRecurrent(None))
