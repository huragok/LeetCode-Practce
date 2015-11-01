import collections

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return True
        
        children = collections.defaultdict(list) # The children of each node
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])
 
        root = 0
        parent = [None] * n
        # BFS
        queue = [root]
        while queue:
            node = queue.pop(0)
            #print(node)
            #print(parent)
            for child in children[node]:
                if child != parent[node]:
                    if parent[child] is not None and parent[child] != node:
                        return False
                    queue.append(child)
                    parent[child] = node
        #print(parent)
        return sum([(1 if p is None else 0) for p in parent]) == 1
        
if __name__=="__main__":
    #n = 5
    #edges = [[0,1],[0,2],[2,3],[2,4]]
    n = 3
    edges = [[1,0],[2,0]]
    print(Solution().validTree(n, edges))
