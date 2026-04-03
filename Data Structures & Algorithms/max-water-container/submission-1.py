from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        start, end = 0, len(heights) - 1

        while start < end:
            width = end - start
            h = min(heights[start], heights[end])
            max_area = max(max_area, width * h)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_area
