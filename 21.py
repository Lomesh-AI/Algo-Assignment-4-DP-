from typing import List

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 4 != 0:
            return False
        side = total // 4

        nums.sort(reverse=True)

        n = len(nums)

        if nums[0] > side:
            return False

        used = [False] * n
        dp = {}

        def helper(start, sides_left, curr_sum):
            if sides_left == 1:
                return True
            if curr_sum == side:
                return helper(0, sides_left - 1, 0)

            key = (tuple(used), sides_left, curr_sum)
            if key in dp:
                return dp[key]

            for i in range(start, n):
                if not used[i] and curr_sum + nums[i] <= side:
                    used[i] = True
                    if helper(i + 1, sides_left, curr_sum + nums[i]):
                        dp[key] = True
                        return True
                    used[i] = False

            dp[key] = False
            return False

        return helper(0, 4, 0)
