class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        print(n)
        if n == 0:
            return 0
        len_min = n + 1
        ptr_left = 0
        ptr_right = 0
        sum_tmp = nums[0]
        while ptr_left < n:
            while sum_tmp < s:
                ptr_right += 1
                if ptr_right >= n:
                    break
                sum_tmp += nums[ptr_right]
            
            if ptr_right >= n:
                break
            elif len_min > ptr_right - ptr_left + 1:
                len_min = ptr_right - ptr_left + 1
                
            sum_tmp -= nums[ptr_left]
            ptr_left += 1
            
        if len_min == n + 1:
            return 0
        else:
            return len_min
        
        
if __name__ == "__main__":
    nums = [1, 1]
    s = 3
    print(Solution().minSubArrayLen(s, nums))
                
