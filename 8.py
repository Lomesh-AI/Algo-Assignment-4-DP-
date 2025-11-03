class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def helper(ind):
            nonlocal n
            if ind >= n:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            combination = 0 
            maxx = 0
            j = 1
            for i in range(ind, min(n, ind + k)):
                maxx = max(maxx, arr[i])

                combination = max(combination, j * maxx + helper(ind + j))
                j += 1
                
            dp[ind] = combination
            return dp[ind]
        
        dp = [-1 for _ in range(n)]
        return helper(0)           

