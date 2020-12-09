# 10 --> 5 --> 16 --> None

# linkedList = {
#     head: {
#         value: 10,
#         next: {
#             value: 5,
#             next: {
#                 value: 16,
#                 next: None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        string = '{'
        string += 'value: {}, next: {}'.format(self.value, self.next)
        string += '}'
        return string


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def insert(self, index, value):
        if index < self.size and index >= 0:
            if index == 0:
                self.prepend(value)
            else:
                currentNode = self._getNodeAtIndex(index - 1)
                newNode = Node(value)
                nextNode = currentNode.next
                newNode.next = nextNode
                currentNode.next = newNode
                self.size += 1

    def remove(self, index):
        if index < self.size and index >= 0:
            if index == 0:
                self.head = self.head.next
            else:
                currentNode = self._getNodeAtIndex(index - 1)
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                if index == self.size - 1:
                    self.tail = currentNode
            self.size -= 1

    def reverse(self):
        currentNode = self.head
        tmpArray = []

        while currentNode is not None:
            tmpArray.append(currentNode.value) # O(1)
            currentNode = currentNode.next

        arrayLen = len(tmpArray)
        currentNode = self.head

        for i in range(arrayLen - 1, -1, -1):
            currentNode.value = tmpArray[i] #O(1)
            currentNode = currentNode.next
            
    # def reverse(self):
    #     currentNode = self.head
    #     i = 0

    #     while currentNode is not None:
    #         self.prepend(currentNode.value) #O(1)
    #         currentNode = currentNode.next
    #         i += 1

    #     j = self.size *2
    #     while j >= i:
    #         self.remove(j) #O(n)
    #         j -= 1
    
    def _getNodeAtIndex(self, index):
        currentNode = self.head
        for i in range(index):
            if currentNode is not None:
                currentNode = currentNode.next
        return currentNode

    def __str__(self):
        string = ''
        string += '{\n'
        string += '  head:{\n'
        string += '    value: {}\n'.format(self.head.value)
        string += '    next: {}\n'.format(self.head.next)
        string += '  },\n'
        string += '  tail:\n'
        string += '    value: {}\n'.format(self.tail.value)
        string += '    next: {}\n'.format(self.tail.next)
        string += '  }\n'
        string += '  size: {}\n'.format(self.size)
        string += '}\n'
        return string


linkedList = LinkedList(10)
linkedList.append(30)
linkedList.append(40)
linkedList.prepend(0)
# print('Append', linkedList)
linkedList.insert(20, 2)
# print('Insert', linkedList)
linkedList.remove(4)
# print('Remove', linkedList)
linkedList.reverse()
print('Reverse', linkedList)
