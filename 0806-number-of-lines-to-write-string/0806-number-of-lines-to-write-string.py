class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        w = 0
        for ch in s:
            x = widths[ord(ch) - ord('a')]
            if w + x > 100:
                lines += 1
                w = x
            else:
                w += x
        return [lines, w]