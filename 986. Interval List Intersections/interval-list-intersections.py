from typing import List
class Interval:
    def __init__(self, range: List):
        self.start = range[0]
        self.end = range[1]
        
def has_intersection(interval1: Interval, interval2: Interval):
    if interval1.start > interval2.end or interval2.start > interval1.end:
        return False

    return True

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i1, i2 = 0, 0
        intersections = []
        while i1 < len(firstList) and i2 < len(secondList):
            intval1 = Interval(firstList[i1])
            intval2 = Interval(secondList[i2])
            if has_intersection(intval1, intval2):
                start = max(intval1.start, intval2.start)
                end = min(intval1.end, intval2.end)
                intersections.append([start, end])

            # move the one that has the smaller end, remember to check for end of List
            if intval2.end > intval1.end:
                # move intval1
                i1 += 1
            else:
                # move intval2
                i2 += 1
                
        return intersections
    
    