'''
A*
'''
from collections import deque, namedtuple
import heapq
Pos = namedtuple("Pos", ['row', 'col'])
State = namedtuple("State", ['f', 'pos', 'steps', 'hammer']) # pos, heuristic

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        GOAL = Pos(m-1, n-1)
        def is_valid(next_pos, k):
            nonlocal m, n, grid
            
            if next_pos.row < 0 or next_pos.row >= m:
                return False
            if next_pos.col < 0 or next_pos.col >= n:
                return False
            if grid[next_pos.row][next_pos.col] and k <= 0:
                # next_pos is brick and has hammer
                return False
            return True
        
        def calc_f(pos, steps): # f = g+h\
            nonlocal GOAL
            h = (GOAL.row - pos.row) + (GOAL.col - pos.col)
            return h + steps
            
        heap = []
        init_s = State(calc_f(Pos(0, 0), 0), Pos(0, 0), 0, k)
        heapq.heappush(heap, init_s)
        added = set()
        added.add((init_s.pos, init_s.hammer))
        while heap:
            cur = heapq.heappop(heap)
            if cur.pos == GOAL:
                return cur.steps
            for direct in map(Pos._make, [(1, 0), (0, 1), (-1, 0), (0, -1)]):
                next_pos = Pos(cur.pos.row + direct.row, cur.pos.col + direct.col)

                if is_valid(next_pos, cur.hammer):
                    next_hammer = cur.hammer - grid[next_pos.row][next_pos.col]
                    if (next_pos, next_hammer) in added:
                        continue
                    new_s = State(calc_f(next_pos, cur.steps+1), next_pos, cur.steps+1, next_hammer)
                    
                    heapq.heappush(heap, new_s)
                    added.add((new_s.pos, new_s.hammer))
                
        return -1
            
                
            
        
        