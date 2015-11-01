class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        if n == 0:
            return True
            
        segmentable = [False] * (n + 1) # segmentable[i] is true if s[0:i] can be segmented
        segmentable[0] = True
        
        for end in range(0, n):
            for start in range(end, -1, -1):
                if s[start : end + 1] in wordDict and segmentable[start]:
                    segmentable[end + 1] = True
                    break
        return segmentable[n]
        
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
