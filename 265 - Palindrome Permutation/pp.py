import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isodd = collections.defaultdict(int)
        for c in s:
            isodd[c] = 1 - isodd[c]
            
        return sum(isodd.values()) <= 1
        
if __name__ == "__main__":
    s = "carerac"
    print(Solution().canPermutePalindrome(s))
    
