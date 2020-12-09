# Create a function that reverses a String
# I.E -> 'I am gonna pass this interview succesfully' becomes:
# yllufseccus weivretni siht ssap annog ma I

def reverseString(string):
    return ''.join(reversed(list(string)))

def reverseString2(string):
    if type(string) == str:
        reversedString = ''
        for i in range (len(string)-1, -1, -1):
            reversedString += string[i] 

        return reversedString
    else:
        return 'The input was not a String'


print(reverseString('I am gonna pass this interview succesfully'))
print(reverseString2(1))
print(reverseString2(None))
print(reverseString2('I am gonna pass this interview succesfully'))
