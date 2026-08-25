class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c1 = 0
        c2 = 0
        for i in moves:
            if i=='U':
                c1+=1
            elif i=='D':
                c1-=1
            elif i=="L":
                c2+=1
            else:
                c2-=1
        return c1==0 and c2==0