# 1 2 3 2 2
# 1 1 1 2
# 1 2 2 3 4 5 3 3 3 1 1
# 1 2   1 1 1 3     2
'''
1. Group consecutive trees
2. Find largest adjacent sum
'''

# [1]
# [1, 2, 3, 2]
# last_index_of[3] = 2
# last_index_of[2] = 1
# 
# [1, 2, 1]
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = len(fruits)
        best = 0
        l = 0
        r = 0
        last_index_of = {}
        while r < length:
            cur_fruit = fruits[r]
            if cur_fruit not in last_index_of and len(last_index_of) == 2:
                in_basket = list(last_index_of.keys())
                f0, f1 = in_basket[0], in_basket[1]
                l = min(last_index_of[f0], last_index_of[f1]) + 1   
                if last_index_of[f0] < last_index_of[f1]:
                    last_index_of.pop(f0)
                else:
                    last_index_of.pop(f1)
                
                
            last_index_of[cur_fruit] = r
            
            best = max(best, r-l+1)
            r += 1
            
        return best
            
             
            
        