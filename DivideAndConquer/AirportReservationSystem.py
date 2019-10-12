"""
Problems:
Airport with a runway system
- Reservation for future landing
- Reserve request specifies landing time t
- Add t to a set R if no other landings are scheduled within k minutes
- What landed before t?

Ideas:
- Solve this problem using BST data structure
    - Search BST for place to insert: O(Lg n)
    - Insert: O(1)
"""
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.numOfBelowNodes = 0
        self.left = None
        self.right = None


def build_bst_from_sorted_list(nums):
    if not nums:
        return None

    if len(nums) == 1:
        return TreeNode(list[0])

    return helper(nums, 0, len(nums) - 1)


def helper(nums, min, max):
    """
    Recursive generate BST.
    - Start from middle element
    - Left sub-tree is generated from nums[min:mid-1]
    - Right sub-tree is generated from nums[mid+1:max]
    :param nums: list of number to generate BST
    :param min: minimum index
    :param max: maximum index
    :return: BST
    """
    if min > max:
        return None

    mid = (min + max) // 2
    node = TreeNode(nums[mid])
    node.left = helper(nums, min, mid - 1)
    node.right = helper(nums, mid + 1, max)

    return node


def reserve_landing(node, time, k):
    """
    Find correct position to add time to BST. Must satisfy k minutes check
    :param time: time to add to BST tree
    :param k: constraint to check
    :param node: root of BST tree
    :return:
    """
    if not node:
        return TreeNode(time)

    if time < node.val:
        if node.val - time <= k:
            return node
        else:
            node.left = reserve_landing(node.left, time, k)
    elif time > node.val:
        if time - node.val <= k:
            return node
        else:
            node.right = reserve_landing(node.right, time, k)
    else:
        return node

    return node


def traverse_bst(root):
    if not root:
        print(root)
        return

    print(root.val, root.numOfBelowNodes)
    traverse_bst(root.left)
    traverse_bst(root.right)


def assign_num_of_below_nodes(node):
    if not node:
        return 0

    num_left = assign_num_of_below_nodes(node.left)
    num_right = assign_num_of_below_nodes(node.right)
    node.numOfBelowNodes = num_left + num_right + 1

    return node.numOfBelowNodes


def get_num_of_plane_landed_before(node, time, res):
    """
    Walk down tree to find desired time
    Add in 1 for the nodes that are smaller
    Add in the sub-tree size to the left of just compared node
    """
    if not node:
        return res

    if time < node.val:
        return get_num_of_plane_landed_before(node.left, time, res)

    nums_nodes_below_left_node = node.left.numOfBelowNodes if node.left else 0
    return get_num_of_plane_landed_before(node.right, time, res + 1 + nums_nodes_below_left_node)


class Test(unittest.TestCase):
    def test_normal(self):
        nums = [42, 60, 65, 70, 80]
        node = build_bst_from_sorted_list(nums)

        reserve_landing(node, 50, 3)
        reserve_landing(node, 46, 3)
        # won't added to BST
        reserve_landing(node, 41, 3)
        assign_num_of_below_nodes(node)
        # traverse_bst(node)

        self.assertEqual(get_num_of_plane_landed_before(node, 71, 0), 6, "Should return a correct result")
        self.assertEqual(get_num_of_plane_landed_before(node, 62, 0), 4, "Should return a correct result")
        self.assertEqual(get_num_of_plane_landed_before(node, 90, 0), 7,
                         "Should return number of nodes for time greater than all times in BST")
        self.assertEqual(get_num_of_plane_landed_before(node, 40, 0), 0, "Should return 0 for time that less than all times in BST")