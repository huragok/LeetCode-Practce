# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        node_new = UndirectedGraphNode(node.label)
        # BFS to copy
        node.color = 0 # 0 added to the queue, 1 all its neighbors added to the queue, no this property means it has not been probed yet
        q = [node]
        q_new = [node_new]
        node_set = {node_new.label: node_new}
        while q:
            s = q.pop(0)
            s_new = q_new.pop(0)
            for d in s.neighbors:
                if not hasattr(d, 'color'):
                    d.color = 0
                    q.append(d)
                    d_new = UndirectedGraphNode(d.label)
                    s_new.neighbors.append(d_new)
                    q_new.append(d_new)
                    node_set[d.label] = d_new
                elif d == s and s.color == 0:
                    s_new.neighbors.append(s_new)
                else:
                    s_new.neighbors.append(node_set[d.label])
            s.color = 1
              
        return node_new
