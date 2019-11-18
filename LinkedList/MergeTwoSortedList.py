"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
import unittest


def merge_two_sorted_lists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1

    dummy_node = ListNode(0)
    tail = dummy_node

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy_node.next


def linked_list_to_list(l):
    res = []

    while l:
        res.append(l.val)
        l = l.next

    return res


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Test(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        n11 = ListNode(1)
        n12 = ListNode(2)
        n13 = ListNode(4)
        n11.next = n12
        n12.next = n13

        n21 = ListNode(1)
        n22 = ListNode(3)
        n23 = ListNode(4)
        n21.next = n22
        n22.next = n23

        result = merge_two_sorted_lists(n11, n21)
        self.assertEqual([1, 1, 2, 3, 4, 4], linked_list_to_list(result), "Should return merged list correctly")


        n21 = ListNode(1)
        n22 = ListNode(3)
        n23 = ListNode(4)
        n21.next = n22
        n22.next = n23

        result = merge_two_sorted_lists(None, n21)
        self.assertEqual([1, 3, 4], linked_list_to_list(result), "Should return merged list correctly when l1 is None")


        n11 = ListNode(1)
        n12 = ListNode(2)
        n13 = ListNode(4)
        n11.next = n12
        n12.next = n13

        n21 = ListNode(1)
        n22 = ListNode(3)
        n23 = ListNode(4)
        n24 = ListNode(14)
        n25 = ListNode(24)
        n26 = ListNode(34)
        n21.next = n22
        n22.next = n23
        n23.next = n24
        n24.next = n25
        n25.next = n26

        result = merge_two_sorted_lists(n11, n21)
        self.assertEqual([1, 1, 2, 3, 4, 4, 14, 24, 34], linked_list_to_list(result),
                         "Should return merged list correctly when there is lot longer list than other")

        n11 = ListNode(-5)
        n12 = ListNode(-2)
        n13 = ListNode(4)
        n11.next = n12
        n12.next = n13

        n21 = ListNode(-3)
        n22 = ListNode(0)
        n23 = ListNode(3)
        n21.next = n22
        n22.next = n23

        result = merge_two_sorted_lists(n11, n21)
        self.assertEqual([-5, -3, -2, 0, 3, 4], linked_list_to_list(result),
                         "Should return merged list correctly when there are negative values")