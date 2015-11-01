class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        n = len(s)
        return self._partition(s, n, 0, [])
        
    # Partition s[head:] into palindromes (n is the length of s)
    def _partition(self, s, n, head, partial):
        if head == n: # Partition completed
            return [partial]
        else:
            result = []
            for l in range(1, n - head + 1):
                if self._isPalindrome(s[head : head + l], l):
                    partial_new = partial + [s[head : head + l]]
                    result += self._partition(s, n, head + l, partial_new)
            return result
                
    # l is the length of s
    def _isPalindrome(self, s, l):
        for idx in range(l / 2):
            if s[idx] != s[-idx - 1]:
                return False
        return True
        
if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
