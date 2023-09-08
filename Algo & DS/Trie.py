class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_leaf = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_leaf

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def find_words(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        words = []
        self.dfs(curr, prefix, words)
        return words

    def dfs(self, node, word, words):
        if node.is_leaf:
            words.append(word)

        for char, child_node in node.children.items():
            self.dfs(child_node, word + char, words)


def main():
    """
    Driver code to test the implementation.
    """
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.starts_with("app")) # returns true
    trie.insert("app")
    trie.insert("application")
    trie.insert("appropriate")
    print(trie.find_words("app"))
    print(trie.search("app"))  # returns true


if __name__ == "__main__":
    main()
