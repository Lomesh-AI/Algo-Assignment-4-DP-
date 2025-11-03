from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        memo_left = {}
        memo_right = {}

        def left_helper(i):
            if i == 0:
                return 0
            if i in memo_left:
                return memo_left[i]

            if arr[i - 1] < arr[i]:
                memo_left[i] = 1 + left_helper(i - 1)
            else:
                memo_left[i] = 0
            return memo_left[i]

        def right_helper(i):
            if i == n - 1:
                return 0
            if i in memo_right:
                return memo_right[i]

            if arr[i + 1] < arr[i]:
                memo_right[i] = 1 + right_helper(i + 1)
            else:
                memo_right[i] = 0
            return memo_right[i]

        max_len = 0
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = left_helper(i)
                right = right_helper(i)
                max_len = max(max_len, left + right + 1)

        return max_len if max_len >= 3 else 0
