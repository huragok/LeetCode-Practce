class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        candidates = range(1, 10)
        comb = self._combinationSum3(k, n, candidates, [])
        return comb
        
    def _combinationSum3(self, k, n, candidates, selected):
        if candidates == []:
            return []
            
        if k == 1:
            if n not in candidates:
                return []
            else:
                return [selected + [n]]   
        else:
            c = candidates[0]
            #print((n, k))
            #print(candidatis)
            return self._combinationSum3(k - 1, n - c, candidates[1:], selected + [c]) + self._combinationSum3(k, n, candidates[1:], selected)
            
if __name__ == "__main__":
    k = 3
    n = 9
    x = Solution().combinationSum3(k, n)
    print(x)
                
