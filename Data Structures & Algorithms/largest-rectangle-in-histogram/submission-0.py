class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        while stack:
            top = stack.pop()
            height = heights[top]

            if not stack:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1

            area = height * width
            max_area = max(max_area, area)

        return max_area