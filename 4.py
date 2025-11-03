class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = {}

        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        def helper(i, j):
            if i == j:
                return 1

            if i > j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]    

            res = helper(i+1, j) + helper(i, j-1) - helper(i+1, j-1)

            if pal[i][j]:
                res += 1

            dp[(i, j)] = res
            return res        

        return helper(0, n-1) 
           

                       