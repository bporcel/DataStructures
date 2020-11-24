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
        # TODO: Insert method

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
linkedList.append(5)
linkedList.append(16)
linkedList.prepend(1)
print(linkedList)
