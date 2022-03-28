'''
points[i] = [x_i, y_i]
At most 500 points 
0 <= x ,y <= 4* 10^4
'''
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # row_to_col = defaultdict(set)
        # col_to_row = defaultdict(set)
        p_set = set()
        for p in points:
            row, col = p
            # row_to_col[row].add(col)
            # col_to_row[col].add(row)
            p_set.add((row, col))
        min_area = math.inf
        

                
        for i, (r1, c1) in enumerate(points):
            for j, (r2, c2) in enumerate(points[i+1:]):
                if r1 == r2 or c1 == c2:
                    continue
                else:

                    if (r1, c2) in p_set and (r2, c1) in p_set:
                        min_area = min(min_area, abs(r2-r1) * abs(c2-c1))
        
    
        return min_area if min_area != math.inf else 0
                
            