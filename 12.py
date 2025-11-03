class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        def helper(ind):
            if ind == n:
                return 0

            if ind >= n:
                return float('inf')

            if dp[ind] != -1:
                return dp[ind]     

            cost = float('inf')
            for i in range(ind + 1, min(ind+4, n+1)):
                temp = costs[i-1] + (i - ind)**2 + helper(i)
                cost = min(cost, temp)
            dp[ind] = cost
            return cost

        dp = [-1]*n
        return helper(0)  

