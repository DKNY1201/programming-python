class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            self.helper(root, preorder[i])

        return root

    def helper(self, root, n):
        # print(root and root.val)
        # print(n)
        if not root:
            return TreeNode(n)

        if n < root.val:
            root.left = self.helper(root.left, n)
        else:
            root.right = self.helper(root.right, n)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


s = Solution()
preorder = [8,5,1,7,10,12]
s.bstFromPreorder(preorder)