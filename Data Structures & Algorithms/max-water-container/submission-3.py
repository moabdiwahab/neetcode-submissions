class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0

        rigth = len(heights)-1

        max_area = 0

        while left < rigth :

            width = rigth - left

            height_left = heights[left]

            height_right = heights[rigth]

            min_water = min(height_right , height_left)

            area = width * min_water

            max_area = max(max_area, area)


            if height_left < height_right:
                left += 1

            else:
                rigth -= 1

        return max_area












