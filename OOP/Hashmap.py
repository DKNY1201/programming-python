import unittest


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hashmap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __generate_hash_key(self, key):
        return key % self.size

    def get(self, key):
        hash_key = self.__generate_hash_key(key)
        items = self.table[hash_key]

        for item in items:
            if item.key == key:
                return item.value

        raise Exception("Key doesn't exist")

    def set(self, key, value):
        hash_key = self.__generate_hash_key(key)
        items = self.table[hash_key]

        for item in items:
            if item.key == key:
                item.value = value
                return

        items.append(Item(key, value))

    def remove(self, key):
        hash_key = self.__generate_hash_key(key)
        items = self.table[hash_key]

        for i, item in enumerate(items):
            if item.key == key:
                items.pop(i)
                return

        raise Exception("Key doesn't exist")


class HashmapTest(unittest.TestCase):
    def test_hashmap(self):
        hashmap = Hashmap(3)
        hashmap.set(1, 1)
        hashmap.set(2, 2)
        hashmap.set(3, 3)
        hashmap.set(4, 4)
        hashmap.set(5, 5)
        hashmap.set(6, 6)
        hashmap.set(1, 'A')
        hashmap.remove(2)
        hashmap.remove(3)

        self.assertEqual(hashmap.get(1), 'A', 'correct get operation')
        self.assertEqual(hashmap.get(6), 6, 'correct get operation')
        self.assertRaises(Exception, hashmap.get, 2)
        self.assertRaises(Exception, hashmap.remove, 3)
