class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        count1 = 0
        count0 = 0
        for n in nums:
            count0 = (n ^ count0) & (~count1)
            count1 =  (n ^ count1) & (~count0)
            print(count0, count1)
        return count0 | count1
        
if __name__ == "__main__":
    nums = [2,2,3,2]
    print(Solution().singleNumber(nums))
