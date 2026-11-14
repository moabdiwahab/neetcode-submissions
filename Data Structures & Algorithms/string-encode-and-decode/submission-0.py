class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:

            result += str(len(word)) + "#" + word
        
        return result




    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):

            delimter = s.find("#" , i)


            length = int(s[i:delimter])

            word = s[delimter + 1 : delimter + 1 + length]

            result.append(word)

            i = delimter + 1 + length 
        
        return result



        


