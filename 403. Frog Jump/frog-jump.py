'''
jump(pos, prev_k) = 
k = prev_k-1 or prev_k or prev_k+1
if k > 0:
jump(pos, prev_k) = jump(pos+k, k)

'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        @cache
        def jump(pos, prev_k):
            if pos not in stones_set:
                return False
            
            if pos == stones[-1]:
                return True
            next_k = [prev_k-1, prev_k, prev_k+1]
            can_jump = False
            for k in next_k:
                if k <= 0:
                    continue
                can_jump |= jump(pos+k, k)
                if can_jump:
                    return True
                
            return False
        
        
        return jump(stones[0], 0)