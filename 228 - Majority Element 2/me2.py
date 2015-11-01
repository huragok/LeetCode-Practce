class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        N = len(nums)
        if N == 0:
            return []
        elif N == 1:
            return [nums[0]]
        elif N == 2:
            return nums if nums[0] != nums[1] else [nums[0]]
        
        candidate_1 = None
        count_1 = 0
        candidate_2 = None
        count_2 = 0
        
        for n in nums:
            if count_1 > 0 and n == candidate_1:
                count_1 += 1
            elif count_2 > 0 and n == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = n
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = n
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        print(candidate_1, candidate_2)
        print(count_1, count_2)
               
        c_1 = 0
        c_2 = 0
        for n in nums:
            if count_1 > 0 and n == candidate_1:
                c_1 += 1
            if count_2 > 0 and n == candidate_2:
                c_2 += 1
                
        result = []
        if c_1 > N / 3:
            result.append(candidate_1)
        if c_2 > N / 3:
            result.append(candidate_2)
        return result
        
if __name__ == "__main__":
    nums = [6,5,5]
    print(Solution().majorityElement(nums))
