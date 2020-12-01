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
        self.prev = None

    def __str__(self):
        string = '{'
        string += 'value: {}, next: {}, prev: {}'.format(
            self.value, self.next, self.prev.value if self.prev is not None else None)
        string += '}'
        return string


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail # Different from singlyLinkedLists
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def prepend(self, value):
        newNode = Node(value)
        self.head.prev = newNode # Different from singlyLinkedLists
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
                nextNode.prev = newNode # Different from singlyLinkedLists
                newNode.next = nextNode
                newNode.prev = currentNode # Different from singlyLinkedLists
                currentNode.next = newNode
                self.size += 1

    def remove(self, index):
        if index < self.size and index >= 0:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            else:
                currentNode = self._getNodeAtIndex(index - 1)
                NodeToRemove = currentNode.next
                NodeToRemove.prev = currentNode # Different from singlyLinkedLists
                currentNode.next = NodeToRemove.next
                if index == self.size - 1:
                    self.tail = currentNode
            self.size -= 1

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
        string += '    prev: {}\n'.format(self.head.prev)
        string += '  },\n'
        string += '  tail:\n'
        string += '    value: {}\n'.format(self.tail.value)
        string += '    next: {}\n'.format(self.tail.next)
        string += '    prev: {}\n'.format(self.tail.prev)
        string += '  }\n'
        string += '  size: {}\n'.format(self.size)
        string += '}\n'
        return string


linkedList = LinkedList(1)
linkedList.append(3)
linkedList.append(4)
# print('Append', linkedList)
linkedList.prepend(0)
# print('Preppend', linkedList)
linkedList.insert(2, 2)
# print('Insert', linkedList)
linkedList.remove(4)
print('Remove', linkedList)
