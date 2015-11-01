class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return None
            
        max_prod = nums[0] # The maximum product of a subarray ending at current number
        max_prod_pos = None if nums[0] < 0 else nums[0] # The maximum positive (or zero) product of a subarray ending at current number
        min_prod_neg = None if nums[0] >= 0 else nums[0]# The minimum negative product of a subarray ending at current number
        
        print(max_prod, max_prod_pos, min_prod_neg)
        for idx in range(1, n):
            if nums[idx] >= 0:
                if max_prod_pos is None or max_prod_pos < 1:
                    max_prod_pos_new = nums[idx]
                else:
                    max_prod_pos_new = max_prod_pos * nums[idx]
                
                if nums[idx] == 0 or min_prod_neg == None:
                    min_prod_neg_new = None
                else:
                    min_prod_neg_new = min_prod_neg * nums[idx]
            else:
                if min_prod_neg is None:
                    max_prod_pos_new = None
                else:
                    max_prod_pos_new = min_prod_neg * nums[idx]
                    
                if max_prod_pos is None or max_prod_pos < 1:
                    min_prod_neg_new = nums[idx]
                else:
                    min_prod_neg_new = max_prod_pos * nums[idx]
                    
            max_prod_pos, min_prod_neg = max_prod_pos_new, min_prod_neg_new
            if max_prod_pos > max_prod:
                max_prod = max_prod_pos
                
            if min_prod_neg > max_prod:
                max_prod = min_prod_neg
            print(max_prod, max_prod_pos, min_prod_neg)
                
        return max_prod
        
if __name__ == "__main__":
    nums = [2,-5,-2,-4,3]
    print(Solution().maxProduct(nums))
                    
            
