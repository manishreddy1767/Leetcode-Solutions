class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = ""
        for i in address:
            if i=='.':
                x+='[.]'
            else:
                x+=i
        return x