class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqeuncy = {}

        for num in nums:

            freqeuncy[num] = freqeuncy.get(num , 0) + 1

        
        Bucket = []

        for _ in range(len(nums) + 1):
            Bucket.append([])

        
        for num , count in freqeuncy.items():
            Bucket[count].append(num)


        result = []

        for count in range(len(nums) , 0 , -1):
            for num in Bucket[count]:

                result.append(num) 

                if len(result) == k :
                    return result


"last version it is fastest one"

       