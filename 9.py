class Solution:
    def numTeams(self, arr: List[int]) -> int:
        n = len(arr)
        def helper(ind, taken, direction):
            if taken == 3:
                return 1

            if ind >= n:
                return 0

            if dp[ind][taken][direction] != -1:
                return dp[ind][taken][direction]

            teams = 0
            for j in range(ind+1, n):
                if direction == 0 and arr[j] > arr[ind]:
                    teams += helper(j, taken + 1, direction)

                if direction == 1 and arr[j] < arr[ind]:
                    teams += helper(j, taken + 1, direction)   
            dp[ind][taken][direction] = teams
            return teams

        dp = [[[-1]*2 for _ in range(4)] for _ in range(n)]
        count = 0
        for i in range(n):
            count += helper(i, 1, 1)
            count += helper(i, 1, 0)
        return count        