from bisect import bisect_right

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {}

        def helper(ind, last_jump):
            if ind == n - 1:
                return True

            if (ind, last_jump) in dp:
                return dp[(ind, last_jump)]

            one_less_jump = False
            if last_jump > 1:
                index = bisect_right(stones, stones[ind] + last_jump - 1)
                if index - 1> ind and stones[index - 1] == stones[ind] + last_jump - 1:
                    one_less_jump = True and helper(index - 1, last_jump - 1)

            same_jump = False
            index = bisect_right(stones, stones[ind] + last_jump)
            if index - 1 > ind and stones[index - 1] == stones[ind] + last_jump:
                same_jump = True and helper(index - 1, last_jump)

            one_ahead_jump = False
            index = bisect_right(stones, stones[ind] + last_jump + 1)
            if index - 1 > ind and stones[index - 1] == stones[ind] + last_jump + 1: 
                one_ahead_jump = True and helper(index - 1, last_jump+1)

            dp[(ind, last_jump)] = one_less_jump or same_jump or one_ahead_jump
            return dp[(ind, last_jump)]

        if stones[1] != 1:
            return False

        return helper(1, 1)      



