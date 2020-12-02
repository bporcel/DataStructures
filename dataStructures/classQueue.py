# FIFO -> First In First Out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        string = '    value: {}, next: {}\n'.format(self.value, self.next)
        return string

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def peek(self):
        if self.size > 0:
            return self.first

    def enqueue(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        elif self.size > 0:
            self.last.next = newNode
            self.last = newNode
        
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            if self.size == 0:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next

    def isEmpty(self):
        return True if self.size == 0 else False

    def __str__(self):
        string = '{\n'
        string += '  first:\n{}  last:\n {} size: {}'.format(
            self.first, self.last, self.size)
        string += '\n}'
        return string

queue = Queue()
print('Peek --> ', queue.peek())
print('Empty --> ', queue.isEmpty())
queue.enqueue('Google')
queue.enqueue('Github')
queue.enqueue('StackOverflow')
print('Peek --> ', queue.peek())
print('Empty --> ', queue.isEmpty())
queue.dequeue()
print(queue)