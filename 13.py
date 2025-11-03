class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        pal = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i < 2 or pal[i+1][j-1]):
                    pal[i][j] = True 

        def helper(ind):
            if ind >= n:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            string = ''
            cost = float('inf')
            for i in range(ind, n):
                if pal[ind][i]:
                    cost = min(cost, 1 + helper(i + 1))

            dp[ind] = cost
            return cost        

        dp = [-1]*n
        return helper(0) - 1  
