class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.count = 0
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.count = 1
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
            
        return node.count == 1
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for character in prefix:
            if character not in node.children:
                return False
            node = node.children[character]
            
        return True
        

# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    trie = Trie()
    trie.insert("abc")
    print(trie.search("abc"))
    print(trie.search("ab"))
    trie.insert("ab")
    print(trie.search("ab"))
    trie.insert("ab")
    print(trie.search("ab"))
