import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isword = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for character in word:
            node = node.children[character]
        node.isword = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.result = []
        self.board = board
        self.nrow = len(board)
        if self.nrow < 1:
            return []
        self.ncol = len(board[0])
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
            
        for row in range(self.nrow):
            for col in range(self.ncol):
                self.dfsVisit(row, col, self.trie.root, "")
                
        return self.result
        
    
    def dfsVisit(self, row, col, node, prefix):
       # dfs visit the board starting from (row, col), current pointer in the trie is node and the current path from the root to node (included) is prefix  
        if node.isword:
            self.result.append(prefix)
            node.isword = False
            
        if row < 0 or row >= self.nrow or col < 0 or col >= self.ncol:
            return 
                
        character = self.board[row][col]
        if character in node.children: # Continue the dfs search from its neighbors
            prefix += character
            self.board[row][col] = '@'
            self.dfsVisit(row - 1, col, node.children[character], prefix)
            self.dfsVisit(row + 1, col, node.children[character], prefix)
            self.dfsVisit(row, col - 1, node.children[character], prefix)
            self.dfsVisit(row, col + 1, node.children[character], prefix)
            self.board[row][col] = character

        return
            
            
if __name__ == "__main__":
    words = ["oath","pea","eat","rain"]
    board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]
    print(Solution().findWords(board, words))
        
        
