class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x: x[1])

        def helper(ind, last_end):
            if ind >= n:
                return 0

            if (ind, last_end) in dp:
                return dp[(ind, last_end)]

            pick = 0
            if pairs[ind][0] > last_end:
                pick = 1 + helper(ind + 1, pairs[ind][1])

            not_pick = helper(ind + 1, last_end)
            dp[(ind, last_end)] = max(pick, not_pick) 
            return max(pick, not_pick)

        dp = {}

        return helper(0, float('-inf'))    