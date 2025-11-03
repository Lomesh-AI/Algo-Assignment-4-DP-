class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def helper(ind, partition):
            if partition == 1:
                return sum(nums[ind:])

            # print(ind, partition)
            if dp[ind][partition] != -1:
                return dp[ind][partition]

            summ = 0
            minn = float('inf')

            for i in range(ind, n - 1):
                summ += nums[i] 
                if summ > minn:
                    break
                largest = max(summ, helper(i+1, partition - 1))
                minn = min(minn, largest)

            dp[ind][partition] = minn
            return minn

        dp = [[-1]*(k+1) for _ in range(n)]
        return helper(0, k)        

                