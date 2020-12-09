# LIFO -> Last In First Out

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def peek(self):
        index = len(self.data) -1
        if index >= 0:
            return self.data[index]
        else:
            return None

    def pop(self):
        if len(self.data) > 0:
            self.data.pop()

    def isEmpty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        return str(self.data)
        


stack = Stack()
print('Peek  ---->', stack.peek())
stack.push('Google')
print('Peek  ---->', stack.peek())
stack.push('Github')
stack.push('StackOverflow')
print('After Push -> ', stack)
print('Peek  ---->', stack.peek())
stack.pop()
print('After Pop -> ', stack)
print(stack.isEmpty())
stack.pop()
stack.pop()
print(stack.isEmpty())
