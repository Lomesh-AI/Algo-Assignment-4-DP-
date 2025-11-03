class Solution:
    def twoEggDrop(self, n: int) -> int:

        def helper(egg, floor):
            if egg == 1:
                return floor

            if floor == 1:
                return 1

            if dp[egg][floor] != -1:
                return dp[egg][floor]

            maxx = float('inf')
            for i in range(1, floor+1):
                worst_case = 1 + max(helper(egg-1, i-1), helper(egg, floor - i))

                maxx = min(maxx, worst_case)

            dp[egg][floor] = maxx
            return maxx

        dp = [[-1]*(n+1) for _ in range(3)]
        return helper(2, n)