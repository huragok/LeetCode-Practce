import heapq

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        max_mr = 0
        intervals = sorted(intervals, key = lambda interval: interval.start)
        pq = []
        len_pq = 0
        for interval in intervals:
            while len_pq > 0 and pq[0][1].end <= interval.start:
                heapq.heappop(pq)
                len_pq -= 1
            heapq.heappush(pq, (interval.end, interval))
            len_pq += 1
            max_mr = max([max_mr, len_pq])
            
        return max_mr
        
if __name__ == "__main__":
    intervals = [Interval(i[0], i[1]) for i in [[0, 30],[5, 10],[15, 20]]]
    print(Solution().minMeetingRooms(intervals))
            
