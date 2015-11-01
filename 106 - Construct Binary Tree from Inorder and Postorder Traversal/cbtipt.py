# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
            
        n = len(inorder)
        map_inorder = {item[1]: item[0] for item in enumerate(inorder)}
        return self._buildTree(inorder, postorder, 0, n, 0, n, map_inorder)
        
    def _buildTree(self, inorder, postorder, lp, rp, li, ri, map_inorder):
        if lp >= rp:
            return None
        elif rp - lp == 1:
            return TreeNode(postorder[lp])
            
        divide = postorder[rp - 1]
        pos_divide = map_inorder[divide]
        len_left = pos_divide - li
        
        node = TreeNode(divide)
        node.left = self._buildTree(inorder, postorder, lp, lp + len_left, li, pos_divide, map_inorder)
        node.right = self._buildTree(inorder, postorder, lp + len_left, rp - 1, pos_divide + 1, ri, map_inorder)
        return node
        
if __name__ == "__main__":
    inorder = [1,2,3,4]
    postorder = [3,2,4,1]
    
    x = Solution().buildTree(inorder, postorder)
