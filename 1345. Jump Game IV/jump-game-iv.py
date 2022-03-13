from copy import copy
from typing import List
from collections import deque, namedtuple
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def get_all_idx_of_all_val(arr: List[int]) -> dict:
            all_idx_of_all_val = {}
            for idx, val in enumerate(arr):
                if val not in all_idx_of_all_val:
                    all_idx_of_all_val[val] = []
                all_idx_of_all_val[val].append(idx)
            return all_idx_of_all_val
        
        def is_valid(pos: int, arr: List[int]) -> bool:
            return pos >= 0 and pos < len(arr)
                    
            
        # BFS
        searches = deque()
        Path = namedtuple('Path', ['pos', 'steps'])
        
        GOAL_IDX = len(arr) - 1
        added = set()
        val_explored = set()
        searches.append(Path(0, 0))
        added.add(0) # add starting pos
        
        all_idx_of_all_val = get_all_idx_of_all_val(arr)
        while len(searches):
            cur_pos, cur_steps = searches.popleft()
            cur_val = arr[cur_pos]
            
            if cur_pos == GOAL_IDX:
                return cur_steps
            
            extra_idxs = all_idx_of_all_val[cur_val] if cur_val not in val_explored else []
            for next_pos in [cur_pos-1, cur_pos+1, *extra_idxs]:
                # check if valid & if added
                if is_valid(next_pos, arr) and next_pos not in added:
                    searches.append(Path(pos=next_pos, steps=cur_steps+1))
                    added.add(next_pos)
                    
            val_explored.add(cur_val)
            
            
            
            
        
        
        
                    
        
            