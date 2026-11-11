class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [1] * n 

        suffix = [1] * n 

        current = 1

        for i in range(n):

            prefix[i] = current

            current *= nums[i]


        current = 1

        for i in range(n-1 , -1 , -1):

            suffix[i] = current

            current *= nums[i]

        
        result =  [1] * n 

        for i in range(n):

            result[i] = prefix[i] * suffix[i]

        return result

        