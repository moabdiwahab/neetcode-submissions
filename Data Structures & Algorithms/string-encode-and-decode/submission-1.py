class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            result.append (str(len(word)) + "#" + word)

        return "".join(result)
       



    def decode(self, s: str) -> List[str]:

        result = []

        i = 0
        while i < len(s):
            delimater = s.find("#" , i)

            length = int(s[i:delimater])

            start = delimater + 1

            end = start + length

            word = s[start:end]

            result.append(word)

            i = start + length

        return result


    





       