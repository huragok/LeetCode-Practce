class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        n = len(nums)
        if n == 0:
            return []
            
        left_bound = nums[0]
        num_last = nums[0]
        intervals = []
        for idx in range(n):
            if nums[idx] > num_last + 1: # Start a new interval
                intervals.append((left_bound, num_last))
                left_bound = nums[idx]
            num_last = nums[idx]
        intervals.append((left_bound, num_last))
        return map(lambda x: str(x[0]) if x[0] == x[1] else str(x[0]) + "->" + str(x[1]), intervals)
        
if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))
