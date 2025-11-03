class Solution:
    def canIWin(self, n: int, total: int) -> bool:
        if total <= 0:
            return True
        if n * (n + 1) // 2 < total:
            return False

        dp = {}

        def helper(used, curr_sum):
            if curr_sum >= total:
                return False

            if used in dp:
                return dp[used]

            for i in range(1, n + 1):
                if not (used >> i) & 1: 
                    new_used = used | (1 << i)
                    if curr_sum + i >= total or not helper(new_used, curr_sum + i):
                        dp[used] = True
                        return True

            dp[used] = False
            return False

        return helper(0, 0)
