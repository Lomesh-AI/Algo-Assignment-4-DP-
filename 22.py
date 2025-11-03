class Solution:
    def minNumberOfSemesters(self, n: int, deps: List[List[int]], k: int) -> int:
        pre = [0] * n
        for u, v in deps:
            pre[v - 1] |= 1 << (u - 1)

        dp = [-1] * (1 << n)

        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0
            if dp[mask] != -1:
                return dp[mask]

            ready = 0
            for i in range(n):
                if (mask >> i) & 1 == 0 and (pre[i] & mask) == pre[i]:
                    ready |= 1 << i

            if bin(ready).count("1") <= k:
                dp[mask] = 1 + dfs(mask | ready)
                return dp[mask]

            best = float("inf")
            sub = ready
            while sub:
                if bin(sub).count("1") == k:
                    best = min(best, 1 + dfs(mask | sub))
                sub = (sub - 1) & ready
            dp[mask] = best
            return best

        return dfs(0)
