class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        if n < 2:
            return [1]
            
        result = [1] * n
        for idx in xrange(1, n):
            result[idx] = result[idx - 1] * nums[idx - 1]
            
        prod = 1
        for idx in xrange(n - 1, -1, -1):
            result[idx] = result[idx] * prod
            prod *= nums[idx]
        
        return result
        
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
