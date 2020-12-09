def reverseString(string):
    if len(string) == 1:
        return string

    return reverseString(string[1:]) + string[:1]

print(reverseString('Hackø'))

# print('Hackø'[:1])  # H
# print('Hackø'[1:])  # ackø
# print('Hackø'[-1:]) # ø 
# print('Hackø'[:-1]) # Hak