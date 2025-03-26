class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.is_end = False  # Marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # Mark end of a word

    def find_prefix(self, prefix):
        """Finds the node where the prefix ends."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None  # Prefix not found
            node = node.children[char]
        return node  # Return the node corresponding to the last prefix character

    def collect_words(self, node, prefix):
        """Recursively collect words from a given node."""
        words = []
        if node.is_end:
            words.append(prefix)

        for char, next_node in node.children.items():
            words.extend(self.collect_words(next_node, prefix + char))

        return words

    def autocomplete(self, prefix):
        """Returns all words with the given prefix."""
        node = self.find_prefix(prefix)
        if not node:
            return []  # No words match the prefix
        return self.collect_words(node, prefix)

if __name__ == "__main__":
# Example Usage
    trie = Trie()
    words = ["dog", "deer", "deal"]
    for word in words:
        trie.insert(word)

    print(trie.autocomplete("de"))  # Output: ['deer', 'deal']
    print(trie.autocomplete("do"))  # Output: ['dog']
    print(trie.autocomplete("ca"))  # Output: []