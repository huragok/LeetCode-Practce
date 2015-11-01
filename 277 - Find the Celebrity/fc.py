# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = set(range(n))
        # Each time randomly pick two people from the candidate set by asking them 1 person can be removed
        for idx in xrange(n - 1):
            a = candidate.pop()
            b = candidate.pop()
            if knows(a, b): # a cannot be the celebrity
                candidate.add(b)
            else:
                candidate.add(a)
                
        # Verify whether the rest guy is a celebrity
        p = candidate.pop()
        for idx in xrange(n):
            if idx != p and ((not knows(idx, p)) or knows(p, idx)):
                return -1
                
        return p
                
