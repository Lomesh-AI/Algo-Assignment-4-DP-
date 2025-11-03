class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(ind):
            if ind >= n:
                return (0, 0)

            count = 1
            max_length = 1

            if dp[ind] != -1:
                return dp[ind]

            for i in range(ind+1, n):
                if nums[i] > nums[ind]:
                    cnt, l = helper(i)

                    if l + 1 > max_length:
                        max_length = l + 1
                        count = cnt

                    elif l + 1 == max_length:
                        count += cnt
            dp[ind] = (count, max_length)
            return (count, max_length)   

        dp = [-1]*n

        count = 0
        max_length = 0
        for i in range(n):
            cnt, l = helper(i)
            
            if l > max_length:
                max_length = l
                count = cnt
            elif l == max_length:
                count += cnt

        return count    
