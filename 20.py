from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)

        if nums[0] > target:
            return False

        used = [False] * n
        dp = {}

        def helper(start, k_remaining, curr_sum):
            if k_remaining == 1:
                return True
            if curr_sum == target:
                return helper(0, k_remaining - 1, 0)

            key = (tuple(used), k_remaining, curr_sum)
            if key in dp:
                return dp[key]

            for i in range(start, n):
                if not used[i] and curr_sum + nums[i] <= target:
                    used[i] = True
                    if helper(i + 1, k_remaining, curr_sum + nums[i]):
                        dp[key] = True
                        return True
                    used[i] = False

            dp[key] = False
            return False

        return helper(0, k, 0)
