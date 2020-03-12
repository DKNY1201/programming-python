import unittest
from collections import deque


def average_values_of_each_level_of_tree(node):
    # each item in queue is the node and its level
    q = deque([(node, 0)])
    result = []
    sum = 0
    nums = 0
    cur_lvl = 0

    while q:
        node, lvl = q.popleft()

        if lvl == cur_lvl:
            sum += node.val
            nums += 1
        else:
            # append the average of previous level
            result.append(sum // nums)
            # reset for next calculation
            sum = node.val
            nums = 1
            cur_lvl = lvl

        if node.left:
            q.append((node.left, lvl + 1))
        if node.right:
            q.append((node.right, lvl + 1))

    # take care the last level
    result.append(sum // nums)

    return result


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Test(unittest.TestCase):
    def test_calc_max_average_subtree(self):
        root = TreeNode(4)
        root1 = TreeNode(7)
        root2 = TreeNode(9)
        root3 = TreeNode(10)
        root4 = TreeNode(2)
        root5 = TreeNode(6)
        root6 = TreeNode(6)
        root7 = TreeNode(2)
        root8 = TreeNode(10)
        root.left = root1
        root.right = root2
        root1.left = root3
        root1.right = root4
        root2.right = root5
        root4.right = root6
        root6.left = root7
        root6.right = root8

        self.assertEqual([4, 8, 6, 6, 6], average_values_of_each_level_of_tree(root),
                         "Should return a list of average values of each level of the tree")