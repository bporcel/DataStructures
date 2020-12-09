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
            isRemove = False
            currentNode = self.root
            previousNode = self._getPreviousNode(currentNode, value, isRemove)
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

    def remove(self, value):
        isRemove = True
        previousNode = self._getPreviousNode(self.root, value, isRemove)
        currentNode = self.root if previousNode is None else self._getCurrentNode(
            value, previousNode)
        isLeaf = False
        onlyLeft = False
        onlyRight = False
        bothChilds = False

        if currentNode.left is None and currentNode.right is None:
            isLeaf = True
        elif currentNode.left is not None and currentNode.right is None:
            onlyLeft = True
        elif currentNode.right is not None and currentNode.left is None:
            onlyRight = True
        elif currentNode.right is not None and currentNode.left is not None:
            bothChilds = True

        if isLeaf:
            self._removeLeaf(previousNode, currentNode)
        elif onlyLeft:
            self._removeLeft(previousNode, currentNode)
        elif onlyRight:
            self._removeRight(previousNode, currentNode)
        elif bothChilds:
            self._removeTraversing(previousNode, currentNode)

    def _removeLeaf(self, previousNode, currentNode):
        if currentNode.value < previousNode.value:
            previousNode.left = None
        else:
            previousNode.right = None

    def _removeLeft(self, previousNode, currentNode):
        if currentNode.value < previousNode.value:
            previousNode.left = currentNode.left
        else:
            previousNode.right = currentNode.left

    def _removeRight(self, previousNode, currentNode):
        if currentNode.value < previousNode.value:
            previousNode.left = currentNode.right
        else:
            previousNode.right = currentNode.right

    def _removeTraversing(self, previousNode, currentNode):
        currentNodePointer = currentNode
        currentNode = currentNode.right
        left = True
        parentNode = None

        while currentNode is not None and left:
            if currentNode.left is None:
                left = False
            else:
                parentNode = currentNode
                currentNode = currentNode.left

        if currentNode.value < previousNode.value:
            if not left:
                if parentNode is not None:
                    if parentNode.left is not None:
                        parentNode.left = currentNode.right

                if currentNodePointer.left is not None:
                    currentNode.left = currentNodePointer.left
                if currentNodePointer.right is not None:
                    currentNode.right = currentNodePointer.right
            previousNode.left = currentNode
        else:
            if not left:
                if parentNode is not None:
                    if parentNode.left is not None:
                        parentNode.left = currentNode.right

                if currentNodePointer.left is not None:
                    currentNode.left = currentNodePointer.left
                if currentNodePointer.right is not None:
                    if currentNode.value != currentNodePointer.right.value:
                        currentNode.right = currentNodePointer.right
            previousNode.right = currentNode

    def _getCurrentNode(self, value, previousNode):
        if previousNode is not None:
            if value < previousNode.value:
                return previousNode.left
            if value > previousNode.value:
                return previousNode.right

    def _getPreviousNode(self, node, value, isRemove):
        while node is not None:
            previousNode = node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            if isRemove:
                if value == self.root.value:
                    return None
                if value == node.value:
                    return previousNode
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
tree.insert(150)
# print('LookUp -> ', tree.lookup(0))
# print('Before Remove', tree.traverse(tree.root))
tree.remove(9)
print('LookUp -> ', tree.lookup(20))
print('After Remove', tree.traverse(tree.root))
