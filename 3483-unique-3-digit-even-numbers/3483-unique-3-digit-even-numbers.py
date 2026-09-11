from itertools import permutations
from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        p = [a*100 + b*10 + c for a, b, c in permutations(digits, 3)]
        for num in p:
            if num not in seen and len(str(num)) == 3:
                if num % 2 == 0:
                    seen.add(num)
        return len(seen)