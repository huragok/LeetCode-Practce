import re, string

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if s == "":
            return True
            
        s = s.lower()
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        n = len(s)
        l = 0
        r = n - 1
        while r - l > 0:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
if __name__ == "__main__":
    s = "race a car"
    print(Solution().isPalindrome(s))
