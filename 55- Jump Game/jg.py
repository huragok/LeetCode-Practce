class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        n = len(nums)
        pos = 0
        step_range = nums[0]
        while pos < n - 1 and step_range > 0:
            max_sum_step = 0
            pos_next = pos
            for step in range(1, step_range + 1):
                if pos + step > n - 1:
                    break
                sum_step_tmp = step + nums[pos + step]
                if sum_step_tmp >= max_sum_step:
                    max_sum_step = sum_step_tmp
                    pos_next = pos + step
            pos = pos_next
            print(pos)
            if pos < n:
                step_range = nums[pos]
                
        if pos >= n - 1:
            return True
        else:
            return False
            
if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))
