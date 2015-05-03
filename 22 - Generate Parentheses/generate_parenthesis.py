#!/usr/bin/env python

def get_nodes(nodes): # Given a list of candidate nodes corresponding to a certain height in the search tree, updates and return a list of child nodes 1 level below that is also active
    nodes_new = [] # Each node represented by a 4-tuple: 1st number is the parenthesis, 2nd number is the left parenthesis remained and 3rd number is the right parenthesis remained, and 4-th number is the number of left parenthesis in the stack
    for node in nodes:
        if node[1] > 0: # Append the left child
            nodes_new.append((''.join((node[0], '(')), node[1] - 1, node[2], node[3] + 1))
        if node[2] > 0 and node[3] > 0:  # Append the right child
            nodes_new.append((''.join((node[0], ')')), node[1], node[2], node[3] - 1))
    return nodes_new

class Solution:
    def generateParenthesis(self, n):
        if n <= 0:
            return set()

        nodes = [('(', n-1, n, 1)] # The first one must be a left parenthesis
        for depth in range(2 * n - 1):
            nodes = get_nodes(nodes)

        return [node[0] for node in nodes]


if __name__ == "__main__":
    n = 3
    x = Solution().generateParenthesis(n)
    print(x)