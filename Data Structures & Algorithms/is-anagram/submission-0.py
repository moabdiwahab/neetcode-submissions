class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency_t = {}

        frequency_s = {}

        for char in s:
            
             frequency_s[char] = frequency_s.get(char , 0) + 1
            

        for char in t :
          
            frequency_t[char] = frequency_t.get(char , 0) + 1
                

            
        return frequency_s == frequency_t
               

        