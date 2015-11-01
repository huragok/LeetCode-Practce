import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
            
        for c in t:
            count[c] -= 1
            
        for n in count.values():
            if n != 0:
                return False
                
        return True
        
        
if __name__ == "__main__":
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))
