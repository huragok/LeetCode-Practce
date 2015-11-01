class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        exist = set()
        for n in nums:
            if n in exist:
                return True
            else:
                exist.add(n)
                
        return False
