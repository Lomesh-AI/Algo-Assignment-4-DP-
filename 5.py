class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}
        def helper(cur_size, copy_size):
            if cur_size == n:
                return 0

            if cur_size > n:
                return 1e8

            if (cur_size, copy_size) in dp:
                return dp[(cur_size, copy_size)]    

            # copy and paste so we have take 2 operations plus
            copy = 2 + helper(2*cur_size, cur_size)

            paste = 1e8
            if copy_size > 0:
                # only paste so only 1 operation plus
                paste = 1 + helper(cur_size + copy_size, copy_size)

            dp[(cur_size, copy_size)] = max(copy, paste) 
            return min(copy, paste)

        return helper(1, 0)        
