class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_columns = len(matrix[0]) 

        left = 0
        right = num_rows*num_columns - 1 

        while(left <= right): 
            mid = left + (right - left) // 2 
            row = mid // num_columns
            col = mid % num_columns

            print(row, col)
            val = matrix[row][col] 

            if val > target: 
                right = mid - 1 
            elif val < target:
                left = mid + 1 
            else: 
                return True 
        return False
            