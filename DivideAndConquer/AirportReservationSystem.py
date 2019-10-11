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

- What landed before t?
    - Walk down tree to find desired time
    - Add in 1 for the nodes that are smaller
    - Add in the sub-tree size to the left of just compared node
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
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

    print(root.val)
    traverse_bst(root.left)
    traverse_bst(root.right)


nums = [42, 60, 65, 70, 80]
node = build_bst_from_sorted_list(nums)
# traverse_bst(node)

reserve_landing(node, 50, 3)
reserve_landing(node, 46, 3)
reserve_landing(node, 41, 3)
traverse_bst(node)