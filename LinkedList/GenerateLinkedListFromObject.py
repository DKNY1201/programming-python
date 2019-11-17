"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
"""
import unittest


def generate_linked_list_from_object(obj):
    if not obj:
        return None

    return helper(obj, {})


def helper(obj, dict):
    if obj:
        id = obj["$id"]
        next = obj["next"]
        randomRef = obj["random"] and obj["random"]["$ref"]
        val = obj["val"]

        ll_node = Node(val)
        dict[id] = ll_node
        ll_node.next = helper(next, dict)
        ll_node.random = dict[randomRef]

        return ll_node

    return None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Test(unittest.TestCase):
    def test_get_max(self):
        obj = {
            "$id": "1",
            "next": {
                "$id": "2",
                "next": None,
                "random": {
                    "$ref": "2"
                },
                "val": 2
            },
            "random": {
                "$ref": "2"
            },
            "val": 1
        }

        result = generate_linked_list_from_object(obj)
        self.assertEqual(1, result.val, "Should return correct head of generated linked list")

        obj = {
            "$id": "1",
            "next": {
                "$id": "2",
                "next": {
                    "$id": "3",
                    "next": {
                        "$id": "4",
                        "next": {
                            "$id": "5",
                            "next": None,
                            "random": {
                                "$ref": "3"
                            },
                            "val": 50
                        },
                        "random": {
                            "$ref": "1"
                        },
                        "val": 40
                    },
                    "random": {
                        "$ref": "5"
                    },
                    "val": 30
                },
                "random": {
                    "$ref": "3"
                },
                "val": 20
            },
            "random": {
                "$ref": "3"
            },
            "val": 10
        }

        result = generate_linked_list_from_object(obj)
        self.assertEqual(10, result.val, "Should return correct head of generated linked list")

        result = generate_linked_list_from_object({})
        self.assertEqual(None, result, "Should return None if object is empty")

        result = generate_linked_list_from_object(None)
        self.assertEqual(None, result, "Should return None if object is None")