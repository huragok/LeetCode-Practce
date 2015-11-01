class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.color = [0] * numCourses
        # self.predecessor = [None] * numCourses
        self.prereq = [set() for course in range(numCourses)]
        for p in prerequisites:
            self.prereq[p[0]].add(p[1])
            
            
        for course in range(numCourses):
            if self.color[course] == 0:
                if not self.dfsVisit(course):
                    return False
                    
        return True
            
    def dfsVisit(self, course):
        self.color[course] = 1
        for course_prereq in self.prereq[course]:
            if self.color[course_prereq] == 1:
                return False
            elif self.color[course_prereq] == 0:
                if not self.dfsVisit(course_prereq):
                    return False
        self.color[course] = 2
        return True
        
            
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))
                            
