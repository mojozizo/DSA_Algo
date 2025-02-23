class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x1,y1 = points.pop()
        dist = 0
        while(len(points)):
            x2,y2 = points.pop()
            dist += max(abs(x2-x1),abs(y2-y1))
            x1,y1 = x2,y2
    
        return dist