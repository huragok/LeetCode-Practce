# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        n = len(nums)
        return self._sortedArrayToBST(nums, 0, n)
        
    def _sortedArrayToBST(self, nums, start, end):
        l = end - start
        if l <= 0:
            return None
        elif l == 1:
            return TreeNode(nums[start])
        
        mid = start + (l - 1) / 2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, start, mid)
        root.right = self._sortedArrayToBST(nums, mid + 1, end)
        return root
