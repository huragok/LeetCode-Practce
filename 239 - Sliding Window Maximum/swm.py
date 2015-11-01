class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        if n == 0 or k == 0 or k > n:
            return []
        dqueue = []
        msw = [0] * (n - k + 1)
        for idx in range(n): 
            while dqueue and nums(dqueue[-1]) <= nums[idx]: # Pop the dqueue from the end to maintain the order
                dqueue.pop()
                
            dqueue.append(idx) # Push the dqueue from the end to add the new max number to it
            # Pop the dequeue from the head as the sliding window moves, at most need to pop 1
            if idx - dqueue[0] >= k:
                dqueue.pop(0)
            
            if idx >= k - 1:
                print(dqueue)
                msw[idx - k + 1] = nums[dqueue[0]]
                
        return msw
                
                
if __name__ == "__main__":
    nums = [1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))
            
                
