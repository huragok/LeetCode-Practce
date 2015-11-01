class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        
        return self._combinationSum2(candidates, target, [])
        
    def _combinationSum2(self, candidates, target, selected):
        if candidates == []:
            return []
            
        c = candidates[0]
        count = 0
        while count < len(candidates) and candidates[count] == c:
            count += 1 # Number of this value
        
        d = target / c    
        
        if c > target:
            return []
            
        result = []
        if d <= count and d * c == target:
            result += [selected + [c] * d]
            
        
        for i in range(count + 1): # In the final results, how many c appears
            result += self._combinationSum2(candidates[count:], target - i * c, selected + [c] * i)
                
        return result
        
if __name__ == "__main__":
    candidates = [4,4,2,1,4,2,2,1,3]
    target = 6
    
    comb = Solution().combinationSum2(candidates, target)
    print(comb)
