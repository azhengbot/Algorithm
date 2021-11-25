class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.l = [[0 for i in range(n+1)] for j in range(m+1)]
        l = self.l
        for i in range(1, m+1):
            for j in range(1, n+1):
                l[i][j] = l[i-1][j] + l[i][j-1] - l[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        l = self.l
        return l[row2][col2] - l[row1-1][col2] - l[row2][col1-1] + l[row1-1][col1-1]
