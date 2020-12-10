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

    def DFSInOrder(self):
        return self.traverseInOrder(self.root, [])
    
    def DFSPreOrder(self):
        return self.traversePreOrder(self.root, [])
   
    def DFSPostOrder(self):
        return self.traversePostOrder(self.root, [])

    def traverseInOrder(self, node, result):
        if node.left is not None:
            self.traverseInOrder(node.left, result)

        result.append(node.value)
        
        if node.right is not None:
            self.traverseInOrder(node.right, result)
        return result
    
    def traversePreOrder(self, node, result):
        result.append(node.value)
        if node.left is not None:
            self.traversePreOrder(node.left, result)
        if node.right is not None:
            self.traversePreOrder(node.right, result)
        return result
        
    def traversePostOrder(self, node, result):
        if node.left is not None:
            self.traversePostOrder(node.left, result)
        if node.right is not None:
            self.traversePostOrder(node.right, result)
        result.append(node.value)
        return result

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
print(tree.DFSInOrder())
print(tree.DFSPreOrder())
print(tree.DFSPostOrder())

#       9
#   4       20
# 1   6  15    170

# DFS
# InOrder ---> [1, 4, 6, 9, 15, 20, 170]
# PreOrder --> [9, 4, 1, 6, 20, 15, 170]
# PostOrder -> [1, 6, 4, 15, 170, 20, 9]
