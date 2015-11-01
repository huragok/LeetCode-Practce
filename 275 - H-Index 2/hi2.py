class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        
        l = -1
        r = n
        while r > l + 1:
            m = (l + r) / 2
            if citations[n - 1 - m] >= m + 1:
                l = m
            else:
                r = m
                
        return l + 1
        
if __name__ == "__main__":
    citations = [0, 1, 3, 5, 6]
    print(Solution().hIndex(citations))
