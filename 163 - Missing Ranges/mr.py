class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        curr_lower = lower
        flag_end = False
        for n in nums:
            curr_upper = n - 1
            if curr_upper > upper:
                curr_upper = upper
                flag_end = True
            if curr_upper > curr_lower:
                ranges.append(str(curr_lower) + "->" + str(curr_upper))
            elif curr_upper == curr_lower:
                ranges.append(str(curr_lower))
            curr_lower = n + 1
            if flag_end:
                break
        if upper > curr_lower:
            ranges.append(str(curr_lower) + "->" + str(upper))
        elif upper == curr_lower:
            ranges.append(str(curr_lower))
            
        return ranges
        
if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75, 190]
    lower = 0
    upper = 99
    
    print(Solution().findMissingRanges(nums, lower, upper))
