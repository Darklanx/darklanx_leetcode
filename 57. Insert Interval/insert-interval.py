class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def is_overlap(intval1, intval2):
            return not (intval1[0] > intval2[1] or intval2[0] > intval1[1])
        
        def merge(intval1, intval2):
            return [min(intval1[0], intval2[0]), max(intval1[1], intval2[1])]    
      
        disjoint_intvals = []    
        large_idx = None
        for idx, intval in enumerate(intervals):
            if intval[0] > newInterval[1]:
                large_idx = idx
                break
                
            if is_overlap(intval, newInterval):
                newInterval = merge(intval, newInterval)
            else:
                disjoint_intvals.append(intval)
                
        disjoint_intvals.append(newInterval)
        if large_idx is not None:
            disjoint_intvals.extend(intervals[large_idx:])
            
        return disjoint_intvals