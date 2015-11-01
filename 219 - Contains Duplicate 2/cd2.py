class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        history = {}
        for idx, n in enumerate(nums):
            if n not in history or idx - history[n] > k:
                history[n] = idx
            else:
                return True
                
        return False
