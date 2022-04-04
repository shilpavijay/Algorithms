'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        newInterval = []
        
        for cur in intervals:
            if not newInterval or newInterval[-1][1] < cur[0]:
                newInterval.append(cur)
            else:
                newInterval[-1][1] = max(newInterval[-1][1],cur[1])
        return newInterval
            
s= Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))     
print(s.merge([[1,4],[4,5]])) 
print(s.merge([[1,4]])) 
print(s.merge([[1,4],[5,6]])) 

       