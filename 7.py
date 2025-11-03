from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        idx = {val: i for i, val in enumerate(arr)}
        dp = {}

        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            prev = arr[j] - arr[i]
            if prev >= arr[i] or prev not in idx:
                return 2

            k = idx[prev]
            length = helper(k, i) + 1
            dp[(i, j)] = length
            return length

        ans = 0
        for j in range(n):
            for i in range(j):
                ans = max(ans, helper(i, j))

        return ans if ans >= 3 else 0
