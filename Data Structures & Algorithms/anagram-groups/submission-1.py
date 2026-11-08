class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            counts = [0] * 26

         
            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1

      
            key = tuple(counts)

           
            if key not in groups:
                groups[key] = []

  
            groups[key].append(word)

        
        return list(groups.values())


        "this takes more efficient than sorting" 

        """
        groups = {}

        for word in strs:

            key = "".join(sorted(word))

            if key not in groups:

                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

        """
        "this is much slower than before"


