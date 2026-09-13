class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = []
        s = s.split()
        for i in s:
            if i.isdigit():
                l.append(int(i))
        for i in range(len(l)-1):
            if l[i+1]<=l[i]:
                return False
        return True