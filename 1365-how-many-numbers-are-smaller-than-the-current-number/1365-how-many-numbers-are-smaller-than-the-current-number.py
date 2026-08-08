class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []                 
        
        for p1 in nums:         
            contador = 0  
            
            for p2 in nums:     
                if p1 > p2:     
                    contador += 1
                    
            l.append(contador)  
            
        return l       
            
       
        