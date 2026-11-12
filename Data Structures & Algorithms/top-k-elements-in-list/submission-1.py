class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqeuncy ={}

        for num in nums:
            freqeuncy[num] = freqeuncy.get(num , 0)+1

        
        buckets = [[] for _ in range(len(nums) + 1 )]

        for num , count in freqeuncy.items():
            buckets[count].append(num)

        result = []

        for count in range(len(nums) , 0 , -1):
            for num in buckets[count]:
                result.append(num)

                
                if len(result) == k :
                    return result
        """
        freqeuncy = {}

        for num in nums:

            if num not in freqeuncy:

                freqeuncy[num] = 1
            else:
                freqeuncy[num] += 1


        
        sorted_item = sorted(
            freqeuncy.items(),
            key=lambda item : item[1],
            reverse=True
        )

        result = []

        for i in sorted_item[:k]:
            result.append(i[0])

        return result

        """



        