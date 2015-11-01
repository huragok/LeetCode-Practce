class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
            
        num_min = min(nums)
        num_max = max(nums)
        buckets_min = {idx: None for idx in range(n)}
        buckets_max = {idx: None for idx in range(n)}
        bucket_size = max((float(num_max - num_min) / float(n - 1), 1.0))
        
        for num in nums:
            idx = int(float(num - num_min) / bucket_size)
            if buckets_min[idx] is None or num < buckets_min[idx]:
                buckets_min[idx] = num
            if buckets_max[idx] is None or num > buckets_max[idx]:
                buckets_max[idx] = num
        print(buckets_max)
        print(buckets_min)
                
        min_gap = 0
        idx_left = 0
        for idx_right in range(1, n):
            if buckets_max[idx_right] is not None:
                if buckets_min[idx_right] - buckets_max[idx_left] > min_gap:
                    min_gap = buckets_min[idx_right] - buckets_max[idx_left]
                idx_left = idx_right
                
        return min_gap
        
if __name__ == "__main__":
    nums = [3,6,9,1]
    print(Solution().maximumGap(nums))
            
