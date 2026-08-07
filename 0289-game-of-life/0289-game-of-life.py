class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        temp = [row[:] for row in board]
        for i in range(n):
            for j in range(m):
                c = 0
                if i-1 >= 0 and j-1 >= 0 and temp[i-1][j-1] == 1:
                    c += 1
                if i-1 >= 0 and temp[i-1][j] == 1:
                    c += 1
                if i-1 >= 0 and j+1 < m and temp[i-1][j+1] == 1:
                    c += 1
                if j-1 >= 0 and temp[i][j-1] == 1:
                    c += 1
                if j+1 < m and temp[i][j+1] == 1:
                    c += 1
                if i+1 < n and j-1 >= 0 and temp[i+1][j-1] == 1:
                    c += 1
                if i+1 < n and temp[i+1][j] == 1:
                    c += 1
                if i+1 < n and j+1 < m and temp[i+1][j+1] == 1:
                    c += 1
                if temp[i][j] == 1:
                    if c < 2 or c > 3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                else:
                    if c == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0