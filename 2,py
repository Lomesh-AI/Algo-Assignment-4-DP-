class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        def helper(i, j):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            same = 0
            different = 0
            if word1[i] == word2[j]:
                same = 1 + helper(i-1, j-1)
            else:
                different = max(helper(i-1, j), helper(i, j-1)) 
            
            dp[i][j] = max(same, different)
            return dp[i][j]

        dp = [[-1]*m for _ in range(n)]
        return n + m - 2*helper(n-1, m-1)   


        # tabulation
        '''dp = [[0]*(m) for _ in range(n)]
        for i in range(n):
            if word1[i] == word2[0]:
                dp[i][0] = 1
            elif i > 0:
                dp[i][0] = dp[i-1][0]    

        for j in range(m):
            if word1[0] == word2[j]:
                dp[0][j] = 1 
            elif j > 0:
                dp[0][j] = dp[0][j-1]           


        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return n + m - 2*dp[n-1][m-1] '''     


        # space otimisation
        # dp = [[0]*(m+1) for _ in range(n+1)]         


        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # return n + m - 2*dp[n][m]     