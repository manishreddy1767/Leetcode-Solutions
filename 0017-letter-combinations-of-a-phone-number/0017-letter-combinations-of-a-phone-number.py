class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
        def solve(index,path):
            if index==len(digits):
                ans.append(path)
                return
            letters=mapping[digits[index]]
            for ch in letters:
                solve(index+1,path+ch)
        ans=[]
        if len(digits)==0:
            return ans
        else:
            solve(0,"")
            return ans
            