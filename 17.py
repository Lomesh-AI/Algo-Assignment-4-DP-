class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        valid_rows = []
        for r in range(m):
            mask = 0
            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)
            valid_rows.append(mask)

        dp = {0: 0}
        for r in range(m):
            next_dp = {}
            valid_mask = valid_rows[r]
            for mask in range(1 << n):
                if (mask & (~valid_mask)) or (mask & (mask << 1)):
                    continue
                for prev_mask, val in dp.items():
                    if mask & (prev_mask << 1) or mask & (prev_mask >> 1):
                        continue
                    next_dp[mask] = max(next_dp.get(mask, 0), val + bin(mask).count('1'))
            dp = next_dp
        return max(dp.values())
