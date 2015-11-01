# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        trees_partial = [[[] for col in range(n + 1)] for row in range(n + 1)] # trees_partial[m][n] is a list containing all trees constructed from m : n
             
        # Initialization
        for l in range(n + 1):
            trees_partial[l][l] = [None]
        for l in range(n):
            trees_partial[l][l + 1] = [TreeNode(l + 1)]
           
        # Update
        for d in range(2, n + 1): # d is the length of the tree
            for l in range(n - d + 1):
                r = l + d
                for i in range(l, r):
                    #print('*****************')
                    #print(l, i, r)
                    #print(len(trees_partial[l][i]), len(trees_partial[i+1][r]))
                    #print("02 = {0}".format(len(trees_partial[0][2])))
                    trees_partial[l][r] += [self._build_tree(i+1, tree_left, tree_right) for tree_left in trees_partial[l][i] for tree_right in trees_partial[i+1][r]]
                    #print("02 = {0}".format(len(trees_partial[0][2])))
                #print(len(trees_partial[l][r]))
        return trees_partial[0][n]
                    
                    
    def _build_tree(self, root_val, left, right):
        root_new = TreeNode(root_val)
        root_new.left = left
        root_new.right = right
        return root_new
        
    def _print_tree(self, root):
        if root is None:
            return
        print("_________________________")
        print("val = {0}".format(root.val))
        
        if root.left is None:
            print("left = None")
        else:
            print("left = {0}".format(root.left.val))
            
        if root.right is None:
            print("right = None")
        else:
            print("right = {0}".format(root.right.val))
            
        self._print_tree(root.left)
        self._print_tree(root.right)
            
if __name__ == "__main__":
    n = 3
    trees = Solution().generateTrees(n)
    
    for n, root in enumerate(trees):
        print("The {0}-th tree _______________________________".format(n))
        Solution()._print_tree(root)
