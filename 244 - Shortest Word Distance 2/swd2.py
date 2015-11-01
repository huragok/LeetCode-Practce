import collections

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.pos = collections.defaultdict(list)
        for idx, word in enumerate(words):
            self.pos[word].append(idx)
            
        self.n = len(words)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx_1 = 0
        idx_2 = 0
        min_dist = self.n
        while idx_1 < len(self.pos[word1]) and idx_2 < len(self.pos[word2]):
            min_dist = min([min_dist, abs(self.pos[word1][idx_1] - self.pos[word2][idx_2])])
            if self.pos[word1][idx_1] < self.pos[word2][idx_2]:
                idx_1 += 1
            else:
                idx_2 += 1
        return min_dist


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    wordDistance = WordDistance(words)
    print(wordDistance.shortest("coding", "practice"))
    print(wordDistance.shortest("makes", "coding"))
