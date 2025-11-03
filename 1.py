class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])

        res = [[float('inf')]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:    
                    if i > 0:
                        res[i][j] = min(res[i][j], 1 + res[i-1][j])
                    if j > 0:
                        res[i][j] = min(res[i][j], 1 + res[i][j-1])

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] != -1:
                    if i < n-1:
                        res[i][j] = min(res[i][j], 1 + res[i+1][j])
                    if j < m-1:
                        res[i][j] = min(res[i][j], 1 + res[i][j+1])

        return res                                        