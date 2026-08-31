class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x = []
        for i in words:
            s=""
            for j in i:
               s+=l[(ord(j)-97)%26]
            x.append(s)
        return len(set(x)) 