#       9
#   4       20
# 1   6  15    170

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        string = 'value: {}\nleft: {}\nright: {}'.format(
            self.value, self.left, self.right)
        return string


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            previousNode = self._getNodeToInsert(currentNode, value)
            if value < previousNode.value:
                previousNode.left = newNode
            elif value > previousNode.value:
                previousNode.right = newNode

    def lookup(self, value):
        currentNode = self.root
        while currentNode is not None:
            if value == currentNode.value:
                return currentNode
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None

    def _getNodeToInsert(self, node, value):
        while node is not None:
            previousNode = node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        return previousNode

    def traverse(self, node):
        if node is not None:
            tree = {'value': node.value, 'left': None, 'right': None}
            tree['left'] = None if node.left == None else self.traverse(
                node.left)
            tree['right'] = None if node.right == None else self.traverse(
                node.right)
            return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
print('LookUp -> ', tree.lookup(0))
print('LookUp -> ', tree.lookup(170))
print(tree.traverse(tree.root))
