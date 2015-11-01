class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0 or n == 1 or n == 2:
            return n
            
        ptr_removed = 0
        ptr_probe = 1
        val_current = nums[0]
        while ptr_probe < n:
            if nums[ptr_probe] != val_current:
                val_current = nums[ptr_probe]
                # remove [count_current - 2]+ values before ptr_probe
                if ptr_probe - ptr_removed > 2:
                    n_remove = ptr_probe - ptr_removed - 2
                    
                    nums[ptr_removed + 2 : ptr_probe] = []
                    ptr_probe -= n_remove
                    n -= n_remove
                    ptr_removed += 2
                else:
                    ptr_removed = ptr_probe

            ptr_probe += 1
            
        if ptr_probe - ptr_removed > 2:
            n_remove = ptr_probe - ptr_removed - 2          
            nums[ptr_removed + 2 : ptr_probe] = []
            n -= n_remove
            
        return n
        
if __name__ == "__main__":
    nums = [1,1,1]
    print(Solution().removeDuplicates(nums))
    print(nums)
