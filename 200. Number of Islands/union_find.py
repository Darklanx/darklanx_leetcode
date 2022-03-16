from collections import namedtuple
Pos = namedtuple("Pos", ['row', 'col'])
class UnionFind:
    def __init__(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.parent = [[Pos(i, j) for j in range(self.n)] for i in range(self.m)]
        self.rank = [[0 for j in range(self.n)] for i in range(self.m)]
        self._init_group()
                
    def _init_group(self):
        self.n_group = 0
        for row in range(self.m):
            for col in range(self.n):
                if self.grid[row][col] == '1':
                    self.n_group += 1
        
    def find_root(self, pos):
        row, col = pos.row, pos.col
        if self.parent[row][col] != (row, col):
            self.parent[row][col] = self.find_root(self.parent[row][col])
            
        return self.parent[row][col]
            
    def union(self, pos1, pos2) -> bool:
        '''
        Returns: whether a union is performed.
        '''
        parent1 = self.find_root(pos1)
        parent2 = self.find_root(pos2)
        if parent1 == parent2:
            return False 
        
        rank1, rank2 = self.get_rank(pos1), self.get_rank(pos2)
        if rank1 > rank2:
            self.increase_rank(parent1)
            self.parent[parent2.row][parent2.col] = parent1
        else:
            self.increase_rank(parent2)
            self.parent[parent1.row][parent1.col] = parent2
            
        self.n_group -= 1
        return True
        
    def get_rank(self, pos):
        root_pos = self.find_root(pos)
        return self.rank[root_pos.row][root_pos.col]
        
    def increase_rank(self, pos):
        root_pos = self.find_root(pos)
        self.rank[root_pos.row][root_pos.col] += 1
        
    def is_valid_pos(self, pos):
        row, col = pos.row, pos.col
        if row < 0 or row >= self.m:
            return False
        if col < 0 or col >= self.n:
            return False
        return True
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(grid)
        for row in range(m):
            for col in range(n):
                if (grid[row][col] == '1'):
                    directions = map(Pos._make, [(1,0), (-1,0), (0,1), (0, -1)])
                    for direct in directions:
                        next_pos = Pos(row + direct.row, col + direct.col)
                        
                        if uf.is_valid_pos(next_pos) and grid[next_pos.row][next_pos.col] == '1':
                            uf.union(Pos(row, col), next_pos)
                            
        return uf.n_group
                            
                        
                        
            
                
                
            
        
        

        