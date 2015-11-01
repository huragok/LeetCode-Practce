# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key = lambda interval: interval.start)
        n = len(intervals)
        for idx in range(1, n):
            if intervals[idx].start < intervals[idx - 1].end:
                return False
                
        return True
