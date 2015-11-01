import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = self.findEdges(words)
        #print(edges)
        
        nodes = self.findNodes(words)
        #print(nodes)
        n = len(nodes) # Number of letters in the alphabets
        
        self.children = collections.defaultdict(set)
        for edge in edges:
            self.children[edge[0]].add(edge[1])
        #print(self.children)
        
        # Perform a topological sort
        self.color = {c: 0 for c in nodes}
        #self.timer = 0
        self.ordered_alphabet = ''
        
        for c in nodes:
            if self.color[c] == 0:
                if not self.dfs(c):
                    return ''
        return self.ordered_alphabet
        
    def findEdges(self, words):
        # Find all edges (b, a) where a is lexicographically prior to b
        n = len(words)
        edges = []
        for idx in xrange(1, n):
            w1 = words[idx - 1]
            w2 = words[idx]
            l = min(len(w1), len(w2))
            idx = 0
            while idx < l and w1[idx] == w2[idx]:
                idx += 1
            if idx < l:
                edges.append((w2[idx], w1[idx]))
        return edges
        
    def findNodes(self, words):
        alpha = set()
        for w in words:
            for c in w:
                alpha.add(c)
                
        return alpha
        
    def dfs(self, letter):
        self.color[letter] = 1
        for child in self.children[letter]:
            if self.color[child] == 1: # Circle detected
                return False
            elif self.color[child] == 0:
                if not self.dfs(child):
                    return False
        #self.timer += 1
        self.color[letter] = 2
        self.ordered_alphabet += letter
        return True
        
if __name__ == "__main__":
    words = ["wrt", 
             "wrf",
             "er",
             "ett",
             "rftt"
            ]
            
    print(Solution().alienOrder(words))
