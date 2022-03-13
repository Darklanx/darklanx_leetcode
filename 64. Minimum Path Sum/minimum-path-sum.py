class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_sum_path = [[0 for j in range(n)] for i in range(m)]
        min_sum_path[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row == 0:
                    if col != 0:
                        min_sum_path[row][col] = min_sum_path[row][col-1] + grid[row][col] 
                else:
                    # from top
                    min_sum_path[row][col] = min_sum_path[row-1][col] + grid[row][col]
                    # from left
                    if col != 0:
                        min_sum_path[row][col] = min(min_sum_path[row][col], \
                                                     min_sum_path[row][col-1] + grid[row][col])
                
        return min_sum_path[-1][-1]
