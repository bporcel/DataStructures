# LIFO -> Last In First Out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        string = '    value: {}, next: {}\n'.format(self.value, self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.top = newNode
            self.bottom = newNode
        elif self.size > 0:
            newNode.next = self.top
            self.top = newNode

        self.size += 1

    def peek(self):
        return self.top

    def pop(self):
        if self.size > 0:
            self.size -= 1
            if self.size == 0:
                self.top = None
                self.bottom = None
            else:
                self.top = self.top.next

    def isEmpty(self):
        return True if self.size == 0 else False

    def __str__(self):
        string = '{\n'
        string += '  top:\n{}  bottom:\n {} size: {}'.format(
            self.top, self.bottom, self.size)
        string += '\n}'
        return string


stack = Stack()
print('Peek  ---->', stack.peek())
stack.push('Google')
print('After Push -> ', stack)
stack.push('Github')
stack.push('StackOverflow')
print('Peek  ---->', stack.peek())
stack.pop()
print('After Pop -> ', stack)
print(stack.isEmpty())
stack.pop()
stack.pop()
print(stack.isEmpty())
