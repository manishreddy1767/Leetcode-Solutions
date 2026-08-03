class Solution:
    def __init__(self):
        self.l = []

    def solve(self, s: str, n: int, o: int, c: int):
        if len(s) == 2 * n:
            self.l.append(s)
            return

        if o < n:
            self.solve(s + '(', n, o + 1, c)

        if c < o:
            self.solve(s + ')', n, o, c + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.l = []
        self.solve("", n, 0, 0)
        return self.l