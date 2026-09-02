class Solution:
    def interpret(self, command: str) -> str:
        x = ""
        for i in range(len(command)-1):
            if command[i].isalpha():
                x+=command[i]
            if command[i]=='(' and command[i+1]==')':
                x+='o'
        if command[-1].isalpha():
            x+=command[-1]
        return x