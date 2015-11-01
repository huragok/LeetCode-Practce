class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        alpha_to_prime = {alphas[n]: primes[n] for n in range(26)}
        
        hash_table1 = self._build_hash_table(s1, alpha_to_prime)
        hash_table2 = self._build_hash_table(s2, alpha_to_prime)
        n = len(s1)
        return self._isScramble(s1, s2, 0, n, 0, n, hash_table1, hash_table2)
        
    def _isScramble(self, s1, s2, l1, r1, l2, r2, hash_table1, hash_table2):
        m = r1 - l1
        n = r2 - l2
        if m != n or hash_table1[(l1, r1)] != hash_table2[(l2, r2)]:
            return False
        elif s1[l1 : r1] == s2[l2 : r2]:
            return True
        elif m == n == 1:
            if s1[l1] == s2[l2]:
                return True
            else:
                return False
        else:
            for i in range(1, m / 2 + 1):
                if self._isScramble(s1, s2, l1, l1+i, l2, l2+i, hash_table1, hash_table2) and self._isScramble(s1, s2, l1+i, r1, l2+i, r2, hash_table1, hash_table2):
                    return True
                elif self._isScramble(s1, s2, l1, l1+i, r2-i, r2, hash_table1, hash_table2) and self._isScramble(s1, s2, l1+i, r1, l2, r2-i, hash_table1, hash_table2):
                    return True
                elif self._isScramble(s1, s2, l1, r1-i, l2+i, r2, hash_table1, hash_table2) and self._isScramble(s1, s2, r1-i, r1, l2, l2+i, hash_table1, hash_table2): 
                    return True
                elif self._isScramble(s1, s2, l1, r1-i, l2, r2-i, hash_table1, hash_table2) and self._isScramble(s1, s2, r1-i, r1, r2-i, r2, hash_table1, hash_table2):
                    return True
            return False
        
    def _build_hash_table(self, s, alpha_to_prime):
        n = len(s)
        hash_table = dict()
        for i in range(n):
            hash_table[(i, i+1)] = alpha_to_prime[s[i]]
        for d in range(2, n + 1):
            for i in range(n + 1 - d):
                hash_table[(i, i+d)] = hash_table[(i, i+d-1)] * alpha_to_prime[s[i+d-1]]
        return hash_table
                    
if __name__=="__main__":
    s1 = "abb"
    s2 = "bab"
    print(Solution().isScramble(s1, s2))
