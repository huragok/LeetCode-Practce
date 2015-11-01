class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.count = 0

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root)

    def _search(self, word, node):
        if len(word) == 1:
            if word[0] == '.': # The last char is '.'
                for character in node.children:
                    if node.children[character].count == 1:
                        return True
                return False
            elif word[0] in node.children and node.children[word[0]].count == 1: # The last char is 'a-z'
                return True
            else:
                return False
        else:
            if word[0] == '.':
                for character in node.children:
                    if self._search(word[1:], node.children[character]):
                        return True
                return False
            else:
                if word[0] not in node.children:
                    return False
                else:
                    return self._search(word[1:], node.children[word[0]])

if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    wordDictionary.addWord("fuck")
    print(wordDictionary.search("."))
