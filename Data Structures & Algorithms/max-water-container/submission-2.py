class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0

        right = len(heights) - 1

        max_area =  0

        while left < right :

            width = right - left 

            left_heights = heights[left]

            right_hight = heights[right]

            min_water = min(right_hight , left_heights)


            area = width * min_water

            max_area = max(max_area , area)


            if left_heights < right_hight :
                left += 1

            else:
                right -= 1

        return max_area