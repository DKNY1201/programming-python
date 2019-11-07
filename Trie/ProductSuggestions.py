"""
Description:
Implement a function to return product suggestions using products from a product repository after each character is typed by the customer in the search bar.
If there are more than THREE acceptable products, return the product name that is first in the alphabetical order.
Only return product suggestions after the customer has entered two characters.
Product suggestions must start with the characters already typed.
Both the repository and the customer query should be compared in a CASE-INSENSITIVE way.

Input:
The input to the method/function consist of three arguments:

numProducts, an integer representing the number of various products in Amazon's product repository;
repository, a list of unique strings representing the various products in Amazon's product repository;
customerQuery, a string representing the full search query of the customer.
Output:
Return a list of a list of strings, where each list represents the product suggestions made by the system as the customer types each character of the customerQuery. Assume the customer types characters in order without deleting/removing any characters.

Example:
Input:
numProducts = 5
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery = "mouse"

Output:
[["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]]

Explanation:
The chain of words that will generate in the search box will be mo, mou, mous and mouse, and each
line from output shows the suggestions of "mo", "mou", "mous" and "mouse", respectively in each line.
For the suggestions that are generated for "mo", the matches that will be generated are:
["mobile", "mouse", "moneypot", "monitor", "mousepad"]. Alphabetically, they will be reordered to
["mobile", "moneypot", "monitor", "mouse", "mousepad"]. Thus, the suggestions are ["mobile", "moneypot", "monitor"]
"""
import unittest


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        current_node = self.root
        val = ""

        for w in word:
            val += w
            if w not in current_node.children:
                current_node.children[w] = TrieNode(val)

            current_node = current_node.children[w]

        current_node.is_word = True

    def search_words_with_prefix(self, prefix):
        current_node = self.root

        for p in prefix:  # O(k)
            if p not in current_node.children:
                return []

            current_node = current_node.children[p]

        words = self.get_words(current_node)  # O(n.l)
        words.sort()  # O(n.logn)

        return words if len(words) <= 3 else words[0:3]

    def get_words(self, node):
        stack = [node]
        res = []

        while stack:
            current_node = stack.pop()

            if current_node.is_word:
                res.append(current_node.val)

            for child in current_node.children.values():
                stack.append(child)

        return res

    # Assume length of query and average length of product name is trivial.
    # Then T(n) = n^2 * logn
    def product_suggestions(self, products, query):
        if len(query) <= 1 or not products:
            return None

        for product in products:  # O(n). n is number of products
            self.insert(product)  # O(l). l is average length of a product name

        custom_queries = []

        for i in range(2, len(query) + 1):  # O(k). k is length of query
            custom_queries.append(query[0:i])

        res = []

        for custom_query in custom_queries:  # O(k)
            res.append(self.search_words_with_prefix(custom_query))  # O(k + n.l + n.logn)

        return res


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False


class Test(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        query = "mouse"
        expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
        self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")

        trie = Trie()
        products = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
                    "standing table", "house", "true love", "tracking device"]
        query = "ps4"
        expected = [["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
        self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
        query = "tru"
        expected = [["tracking device", "true love"], ["true love"]]
        self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
        query = "t"
        self.assertEqual(None, trie.product_suggestions(products, query),
                         "Should return None if query is less than 2 characters")