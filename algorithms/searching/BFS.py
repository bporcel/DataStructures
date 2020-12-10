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

    def breadthFirstSearch(self):
        currentNode = self.root
        result = []
        queue = []
        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue[0]
            result.append(queue[0].value)
            del queue[0]
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        return result

    def breadthFirstSearchRecursive(self, queue, result):
        if len(queue) == 0:
            return result
        currentNode = queue[0]
        result.append(currentNode.value)
        del queue[0]
        if currentNode.left is not None:
            queue.append(currentNode.left)
        if currentNode.right is not None:
            queue.append(currentNode.right)
        return self.breadthFirstSearchRecursive(queue, result)

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
print(tree.breadthFirstSearch())
print(tree.breadthFirstSearchRecursive([tree.root], []))

#       9
#   4       20
# 1   6  15    170
