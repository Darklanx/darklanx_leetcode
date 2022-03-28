class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = 0
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        sum_top = [0 for j in range(n+1)] # at this index, how many consecutive 1s from above
        for i in range(1, m+1):
            sum_left = [0 for j in range(n+1)] # at this index, how many consecutive 1s from left
            for j in range(1, n+1):   
                if matrix[i-1][j-1]:
                    sum_left[j] = sum_left[j-1] + matrix[i-1][j-1]
                    sum_top[j] = sum_top[j] + matrix[i-1][j-1]
                    dp[i][j] = 1 + min(sum_left[j]-1, sum_top[j]-1, dp[i-1][j-1])    
                    count += dp[i][j]
                else:
                    sum_left[j] = 0
                    sum_top[j] = 0
                    
            
        return count