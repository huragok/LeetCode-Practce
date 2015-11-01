import collections

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        count = collections.defaultdict(int)
        for c in citations:
            if c > n:
                count[n] += 1
            else:
                count[c] += 1
        
        cum_count = 0        
        for idx in xrange(n, -1, -1):
            cum_count += count[idx]
            if cum_count >= idx:
                return idx
                
        return 0
        
if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(Solution().hIndex(citations))
