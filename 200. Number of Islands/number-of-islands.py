from collections import namedtuple
from typing import Tuple, Set
Pos = namedtuple("position", ["row", "col"])

def in_2d_bound(grid, pos):
    row, col = pos
    m, n = len(grid), len(grid[0])
    if row >=0 and row < m and col >= 0 and col < n:
        return True
    return False

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_water(grid, pos):
            row, col = pos.row, pos.col
            return grid[row][col] == '0'
        
        def found_island(grid: List[List[str]], pos: Tuple, visited: Set):
            row, col = pos.row, pos.col
            if not in_2d_bound(grid, pos):
                return False
                
            if pos in visited or is_water(grid, pos):
                return False
            
            visited.add(pos)
            directions = map(Pos._make ,[(1, 0), (0, 1), (-1, 0), (0, -1)])
            for direct in directions:
                next_pos = Pos._make(map(sum, zip(pos, direct)))
                found_island(grid, next_pos, visited)
            return True
            
            
        m = len(grid)
        n = len(grid[0])
        n_island = 0
        visited = set()
        
        for row in range(m):
            for col in range(n):
                pos = Pos(row, col)
                n_island += 1*found_island(grid, pos, visited)
        
        return n_island