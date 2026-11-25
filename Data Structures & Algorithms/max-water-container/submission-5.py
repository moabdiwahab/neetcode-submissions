class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0

        right = len(heights) - 1

        max_area = 0

        while left < right:

            width = right - left

            left_height = heights[left]
            right_height = heights[right]

            min_water = min(right_height , left_height)

            area = width * min_water

            max_area = max(area , max_area)

            if left_height < right_height:
                left += 1

            else:
                right -=1 

        return max_area
        