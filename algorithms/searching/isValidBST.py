# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def DFSInOrder(self, node, inOrderList):
        if node.left is not None:
            self.DFSInOrder(node.left, inOrderList)

        inOrderList.append(node.val)

        if node.right is not None:
            self.DFSInOrder(node.right, inOrderList)

        return inOrderList

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inOrderList = root.DFSInOrder(root, [])
        tmp = sorted(inOrderList)
        return inOrderList == tmp

solution = Solution()
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
print(solution.isValidBST(tree))
# -------------------------------
tree = TreeNode(5)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(6)
print(solution.isValidBST(tree))