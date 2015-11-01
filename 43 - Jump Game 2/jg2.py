class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        i = 0
        n = len(nums)
        n_jump = 0
        print(i)
        while i < n - 1:
            step = nums[i]
            
            if i + step >= n - 1:
                return n_jump + 1
                
            max_step_next = nums[i + 1] + 1
            s = 2
            max_s = 1
            while s <= step and i + s < n:
                step_next = nums[i + s] + s
                if max_step_next < step_next:
                    max_step_next = step_next
                    max_s = s
                s += 1     
            
            i += max_s
            print(i)
            n_jump += 1
            
        return n_jump
        
if __name__ == "__main__":
    nums = range(20, -1, -1)
    print(Solution().jump(nums))
