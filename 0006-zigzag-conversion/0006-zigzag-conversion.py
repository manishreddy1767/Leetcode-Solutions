class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        x = ""
        n = len(s)
        cycle = 2 * numRows - 2

        for i in range(numRows):
            for j in range(i, n, cycle):
                x += s[j]
                diag = j + cycle -  i * 2
                if i != 0 and i != numRows - 1 and diag < n:
                    x += s[diag]

        return x