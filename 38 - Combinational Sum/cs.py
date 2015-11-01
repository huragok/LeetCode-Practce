class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        n = len(candidates) # number of candidates
        copy_max = [target / c for c in candidates] # Maximum number of copy of each number
        
        idx = [0] * n
        combination = []
        while True:
            # Check if current sum equals to target
            if sum([idx[i] * candidates[i] for i in range(n)]) == target:
                comb = []
                for i in range(n):
                    if idx[i] > 0:
                        comb += [candidates[i]] * idx[i]
                combination.append(comb)
            
            # update the idx for the next combination
            digit = 0
            while digit < n and idx[digit] == copy_max[digit]:
                idx[digit] = 0
                digit += 1
                
            if digit < n:
                idx[digit] += 1
            else:
                break
                
        return combination
       
if __name__ == "__main__":
    target = 32
    candidates = [7,12,5,10,9,4,6,8]
    comb = Solution().combinationSum(candidates, target)
    print(comb)
