class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        D = range(n + 1) # D[i, j] is the edit distance between word1[0:i] and word1[0:j]
        
        # Initialziation
        for row in range(1, m + 1):
            D[0] = row
            d_lu = row - 1 # D[i - 1, j - 1]
            for col in range(1, n + 1):
                tmp = min([d_lu + (word1[row - 1] != word2[col - 1]), D[col] + 1, D[col - 1] + 1])
                d_lu = D[col]
                D[col] = tmp
                
        return D[-1]
        
if __name__ == "__main__":
    word1 = "a"
    word2 = 'a'
    print(Solution().minDistance(word1, word2))
