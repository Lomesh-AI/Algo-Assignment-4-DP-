class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        nexxt = [[0]*(k+1) for _ in range(2)]  
        cur = [[0]*(k+1) for _ in range(2)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                for transc in range(k):
                    profit = 0
                    if j:
                        profit = max(nexxt[0][transc] - prices[i], nexxt[1][transc])
                    else:
                        profit = max(nexxt[1][transc+1] + prices[i], nexxt[0][transc])
                    cur[j][transc] = profit
            nexxt = cur    

        return cur[1][0]  