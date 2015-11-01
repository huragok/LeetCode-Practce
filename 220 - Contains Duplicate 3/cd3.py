class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        if t == 0:
            return self._containsNearbyDuplicate(nums, k)
        
        bucket = {} # bucket[i] represents i * t : (i + 1) * t, the value is the latest number in this bucket
        for idx, n in enumerate(nums):
            idx_bucket = n / t
            if idx_bucket in bucket:
                return True
            if idx_bucket - 1 in bucket and abs(bucket[idx_bucket - 1] - n) <= t:
                return True
            if idx_bucket + 1 in bucket and abs(bucket[idx_bucket + 1] - n) <= t:
                return True 
                
            bucket[idx_bucket] = n
            
            if idx >= k: # Remove an old bucket
                del bucket[nums[idx - k] / t]
                    
        return False
        
    def _containsNearbyDuplicate(self, nums, k):
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
        
        
if __name__ == "__main__":
    nums = [0,2147483647]
    k = 1
    t = 2147483647
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
