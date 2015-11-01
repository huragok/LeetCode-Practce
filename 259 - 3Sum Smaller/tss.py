class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        count = 0    
        nums = sorted(nums)
        for i in xrange(n - 2):
            j = i + 1
            k = n - 1
            target_residual = target - nums[i]
            while k > j:
                if nums[j] + nums[k] < target_residual:
                    count += 1
                    j += 1
                else:
                    k -= 1
                    
        return count
