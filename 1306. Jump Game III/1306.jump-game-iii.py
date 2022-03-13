from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start > len(arr) or start < 0:
            raise ValueError(f"Invalid starting position: {start}")
        
        def valid(index):
            return index >= 0 and index < len(arr)
            
        def explore(pos: int) -> bool:
            if pos in visited:
                return False
            visited.add(pos)
            if arr[pos] == 0:
                return True
            
            for next_pos in [pos + arr[pos], pos - arr[pos]]:
                if valid(next_pos):
                    if explore(next_pos):
                        return True

        visited = set()

        return explore(start)
