"""
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

Example 1:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
"""

import unittest


class Solution:
    max_average_node = None
    max_avg = -1

    def calc_max_average_subtree(self, root):
        if not root.children:
            return root.val, 1

        total = 0
        n = 0

        for c in root.children:
            tuple = self.calc_max_average_subtree(c)
            total += tuple[0]
            n += tuple[1]

        new_total = total + root.val
        new_n = n + 1
        avg = new_total / new_n

        if avg > self.max_avg:
            self.max_avg = avg
            self.max_average_node = root

        return new_total, new_n


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


class Test(unittest.TestCase):
    def test_calc_max_average_subtree(self):
        s = Solution()
        root = TreeNode(20)
        s.calc_max_average_subtree(root)
        self.assertEqual(None, s.max_average_node, "Should return None if given tree only has 1 node")

        s = Solution()
        root = TreeNode(20)
        root1 = TreeNode(12)
        root2 = TreeNode(18)
        root3 = TreeNode(11)
        root4 = TreeNode(2)
        root5 = TreeNode(3)
        root6 = TreeNode(15)
        root7 = TreeNode(8)
        root.children.append(root1)
        root.children.append(root2)
        root1.children.append(root3)
        root1.children.append(root4)
        root1.children.append(root5)
        root2.children.append(root6)
        root2.children.append(root7)
        s.calc_max_average_subtree(root)
        self.assertEqual(root2, s.max_average_node,
                         "Should correct root that has maximum average subtree")

        s = Solution()
        root = TreeNode(10)
        root1 = TreeNode(40)
        root2 = TreeNode(30)
        root3 = TreeNode(5)
        root4 = TreeNode(6)
        root5 = TreeNode(9)
        root6 = TreeNode(4)
        root7 = TreeNode(100)
        root8 = TreeNode(200)
        root9 = TreeNode(100)
        root.children.append(root1)
        root.children.append(root2)
        root2.children.append(root3)
        root2.children.append(root4)
        root2.children.append(root5)
        root2.children.append(root6)
        root3.children.append(root7)
        root4.children.append(root8)
        root5.children.append(root9)
        s.calc_max_average_subtree(root)
        self.assertEqual(root4, s.max_average_node,
                         "Should correct root that has maximum average subtree")