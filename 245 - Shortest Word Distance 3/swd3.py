class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = len(words)
        if word1 != word2:
            idx_1 = None
            idx_2 = None
            for idx, word in enumerate(words):
                if word == word1:
                    if idx_2 is not None and abs(idx - idx_2) < min_dist:
                        min_dist = abs(idx - idx_2)
                    idx_1 = idx
                elif word == word2:    
                    if idx_1 is not None and abs(idx - idx_1) < min_dist:
                        min_dist = abs(idx - idx_1)
                    idx_2 = idx
        else:
            idx_prev = None
            for idx, word in enumerate(words):
                if word == word1:
                    if idx_prev is not None and abs(idx - idx_prev) < min_dist:
                        min_dist = idx - idx_prev
                    idx_prev = idx
        
        return min_dist

