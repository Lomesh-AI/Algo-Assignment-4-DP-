class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        def helper(egg, floor):
            if egg == 1:
                return floor

            if floor == 1 or floor == 0:
                return floor    

            if dp[egg][floor] != -1:
                return dp[egg][floor]

            low = 1
            high = floor
            minn = float('inf')
            while low <= high:
                mid = (high+ low)//2
                breaks = helper(egg - 1, mid - 1)
                not_break = helper(egg, floor - mid)
                worst_case = 1 + max(breaks, not_break)
                minn = min(minn, worst_case)

                if breaks > not_break:
                    high = mid - 1 
                else:
                    low = mid + 1

            dp[egg][floor] = minn
            return minn

        dp = [[-1]*(n + 1) for _ in range(k+1)]
        return helper(k, n)    
