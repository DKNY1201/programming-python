import unittest


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        val = ""

        for w in word:
            val += w
            if w not in cur.children:
                cur.children[w] = TrieNode(val)
            cur = cur.children[w]

        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        return cur.is_word

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root

        for p in prefix:
            if p in cur.children:
                cur = cur.children[p]
            else:
                return False

        return True

    def get_word_with_prefix(self, prefix):
        """
        Find all words start with prefix
        :param prefix: str
        :return:
        """
        cur = self.root

        for p in prefix:
            if p in cur.children:
                cur = cur.children[p]
            else:
                return []

        words = []
        self.dfs(cur, words)

        return words

    def dfs(self, node, result):
        """
        Get all the words under node and put them into result
        :param node: TrieNode
        :param result: list of words found
        :return:
        """
        if node.is_word:
            result.append(node.val)

        for child in node.children.values():
            self.dfs(child, result)


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False


class Test(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        words = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        trie.insert("mobile")
        trie.insert("mouse")
        trie.insert("moneypot")
        trie.insert("monitor")
        trie.insert("mousepad")

        self.assertTrue(trie.search("mobile"), "Should return True when search word already in trie")
        self.assertTrue(trie.search("mouse"), "Should return True when search word already in trie")
        self.assertTrue(trie.search("mousepad"), "Should return True when search word already in trie")
        self.assertFalse(trie.search("moni"), "Should return False when search word with input is apart of word")
        self.assertTrue(trie.starts_with("moni"), "Should return True when search prefix of word")
        self.assertFalse(trie.starts_with("monis"), "Should return False when search prefix that not in any word")
        self.assertEqual(words.sort(), trie.get_word_with_prefix("mo").sort(),
                         "Should return correct list of word start with provided prefix")
