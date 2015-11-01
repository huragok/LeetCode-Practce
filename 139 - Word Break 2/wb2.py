class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        n = len(s)
        sentences = {}
        return self._wordBreak(s, wordDict, 0, n, sentences)
        
    def _wordBreak(self, s, wordDict, start, n, sentences):
        if start in sentences:
            return sentences[start]
            
        output = []
        if s[start : n] in wordDict:
            output.append(s[start : n])
        for end in range(start + 1, n):
            if s[start : end] in wordDict:
                sentences_partial = self._wordBreak(s, wordDict, end, n, sentences)
                for sentence in sentences_partial:
                    output.append(s[start : end] + " " + sentence)
        sentences[start] = output
        return output
        
if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    s = "abcd"
    wordDict = ["a","abc","b","cd"]
    print(Solution().wordBreak(s, wordDict))
