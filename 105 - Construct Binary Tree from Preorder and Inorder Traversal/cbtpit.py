# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
            
        map_inorder = {item[1]: item[0] for item in enumerate(inorder)}
        n = len(preorder)
        return self._buildTree(preorder, inorder, 0, n, 0, n, map_inorder)
        
    def _buildTree(self, preorder, inorder, lp, rp, li, ri, map_inorder):
        print(lp, rp, li, ri)
        if lp >= rp:
            return None
        elif rp - lp == 1:
            
            return TreeNode(preorder[lp])
            
        divide = preorder[lp]
        pos_divide = map_inorder[divide]
        node = TreeNode(divide)
        len_left = pos_divide - li
        node.left = self._buildTree(preorder, inorder, lp + 1, lp + len_left + 1, li, pos_divide, map_inorder)
        node.right = self._buildTree(preorder, inorder, lp + len_left + 1, rp, pos_divide + 1, ri, map_inorder)
        return node
        
if __name__ == "__main__":
    preorder = [1,2,4,3]
    inorder = [1,2,3,4]
    
    x = Solution().buildTree(preorder, inorder)
