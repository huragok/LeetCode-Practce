class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        axorb = 0
        for num in nums:
            axorb ^= num
            
        mask = (axorb & (axorb - 1)) ^ axorb
        a = 0
        b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
                
        return [a, b]
        
if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(nums))
