class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        self.n = len(nums)
        self.buildHeap()
        print(self.nums)
        
        if k > self.n:
            return None
        tmp = None
        for count in range(k):
            tmp = self.extractMax()
            
        return tmp
        
    def maxHeapify(self, i):
        while i < self.n:
            top = i
            if 2 * i + 1 < self.n and self.nums[top] < self.nums[2 * i + 1]:
                top = 2 * i + 1
                
            if 2 * i + 2 < self.n and self.nums[top] < self.nums[2 * i + 2]:
                top = 2 * i + 2
                
            if top != i:
                self.nums[i], self.nums[top] = self.nums[top], self.nums[i]
                i = top
            else:
                break
        return
                
    
    def buildHeap(self):
        for idx in range(self.n / 2, -1, -1):
            self.maxHeapify(idx)
    
    def extractMax(self):
        if self.n < 0:
            return None
            
        tmp = self.nums[0]
        self.nums[0], self.nums[self.n - 1] = self.nums[self.n - 1], self.nums[0]
        self.n -= 1
        self.maxHeapify(0)
        
        return tmp
        
if __name__ == "__main__":
    nums = [-1, 2, 0]
    k = 3
    print(Solution().findKthLargest(nums, k))
