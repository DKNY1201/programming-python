# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        node1 = node = self.find_node(root, key)
        print(node.val)
        if not node:
            return root

        while node:
            if not node.left and not node.right:
                node = None
            elif node.left:
                node.val = node.left.val
                node = node.left
            else:
                node.val = node.right.val
                node = node.right

        return root

    def find_node(self, root, key):
        while root:
            if root.val == key:
                return root
            elif root.val < key:
                root = root.right
            else:
                root = root.left

        return None

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()
s.deleteNode(root, 3)