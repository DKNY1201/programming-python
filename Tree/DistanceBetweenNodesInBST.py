"""
Given a list of unique integers nums, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes node1 and node2. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.

Example 1:

Input: nums = [2, 1, 3], node1 = 1, node2 = 3
Output: 2
Explanation:
     2
   /   \
  1     3
"""

import unittest


def get_distance_between_nodes_bst(nums, n1, n2):
    if not nums or n1 not in nums or n2 not in nums:
        return -1

    if n1 == n2:
        return 0

    parents = {}

    for num in nums:
        parents[num] = []

    root = TreeNode(nums[0])

    # construct BST
    for i in range(1, len(nums)):
        insert_node(root, nums[i], parents)

    # calculate distance
    parents_n1 = parents[n1]
    parents_n2 = parents[n2]
    l1 = len(parents_n1)
    l2 = len(parents_n2)

    if n1 in parents_n2:
        return l2 - parents_n2.index(n1)
    elif n2 in parents_n1:
        return l1 - parents_n1.index(n2)
    # find lowest common root
    else:
        idx = (l2 if l1 > l2 else l1) - 1

        while idx >= 0 and parents_n1[idx].val != parents_n2[idx].val:
            idx -= 1

        return (l1 - idx) + (l2 - idx)


def insert_node(root, val, parents):
    if not root:
        return TreeNode(val)

    parents[val].append(root)

    if root.val < val:
        root.right = insert_node(root.right, val, parents)
    else:
        root.left = insert_node(root.left, val, parents)

    return root


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Test(unittest.TestCase):
    def test_get_distance_between_nodes_bst(self):
        nums = [2, 1, 3]
        node1 = 1
        node2 = 4
        self.assertEqual(-1, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return -1 when either one or two given nodes are not in bst")

        nums = []
        node1 = 1
        node2 = 4
        self.assertEqual(-1, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return -1 when given numbers are empty")

        nums = [2, 1, 3]
        node1 = 1
        node2 = 3
        self.assertEqual(2, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return correct distance between nodes in bst")

        nums = [4, 6, 9, 11, 1, 2, 5, 7]
        node1 = 1
        node2 = 7
        self.assertEqual(4, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return correct distance between nodes in bst")

        nums = [24, 6, 2, 22, 30, 25, 20, 15, 7, 8, 10, 9, 1]
        node1 = 9
        node2 = 25
        self.assertEqual(10, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return correct distance between nodes in bst")

        nums = [24, 6, 2, 22, 30, 25, 20, 15, 7, 8, 10, 9, 1]
        node1 = 1
        node2 = 9
        self.assertEqual(9, get_distance_between_nodes_bst(nums, node1, node2),
                         "Should return correct distance between nodes in bst")
