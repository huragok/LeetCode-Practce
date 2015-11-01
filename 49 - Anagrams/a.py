class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        n = len(strs)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alpha_to_prime = {alphas[n]: primes[n] for n in range(26)}
        
        strs_value = [self._hash(s, alpha_to_prime) for s in strs]
        group = dict()
        for idx in range(n):
            group.setdefault(strs_value[idx], []).append(strs[idx])
        #print(group)
         
        ana = []
        for g in group.values():
            if len(g) > 1:
                ana += g
        return ana
        
    
    # Map a string to a number factorized by the primes    
    def _hash(self, s, alpha_to_prime):
        p = 1
        for a in s:
            p *= alpha_to_prime[a]
        return p
        
if __name__ == "__main__":
    strs = ['abc', 'cba', 'aab', 'abcd', 'bcad']
    #strs = ['', '']
    print(Solution().anagrams(strs))
