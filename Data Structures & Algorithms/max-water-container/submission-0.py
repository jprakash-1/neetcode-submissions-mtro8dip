class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(heights) - 1

        while start < end: 
            breadth = end - start 
            height = min(heights[start], heights[end])

            area = breadth * height 

            max_area = max(area, max_area)
            if height == heights[start]: 
                start += 1
            
            elif height == heights[end]:
                end -= 1 

        return max_area
