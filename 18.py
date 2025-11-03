class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        dp = {}

        def helper(i):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]

            res = i + 1

            if s[i] == '1':
                res = min(res, helper(i - 1) + 2)
            else:
                res = min(res, helper(i - 1))

            dp[i] = res
            return res

        ans = float('inf')
        for i in range(n):
            ans = min(ans, helper(i) + (n - 1 - i))
        return ans
