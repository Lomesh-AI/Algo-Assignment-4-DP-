class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        def helper(i, j):
            if i < 0  or j < 0:
                return 0

            if matrix[i][j] == 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            above = helper(i-1, j)
            left = helper(i, j-1)
            left_diagonal = helper(i-1, j-1)

            dp[i][j] = 1 + min(above, left, left_diagonal)
            return dp[i][j]

        dp = [[-1]*m for i in range(n)]
        total = 0
        for i in range(n):
            for j in range(m):
                total += helper(i, j)       

        return total      
