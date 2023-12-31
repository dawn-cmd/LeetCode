from typing import List


class Solution:
    # Define method to set zeroes in a matrix
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Check if the first row contains a zero and store the result
        is_first_row_zero = any(num == 0 for num in matrix[0])

        # Check if the first column contains a zero and store the result
        is_first_col_zero = any(nums[0] == 0 for nums in matrix)

        # Iterate over the matrix starting from second row and column
        # If a zero is found, store that information in the corresponding cell in first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Iterate over the matrix again starting from the second row and column
        # If the first cell in the current row or column is zero, set the current cell to zero
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # If the first row originally contained a zero, set the entire first row to zero
        if is_first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        # If the first column originally contained a zero, set the entire first column to zero
        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        # The method does not return anything as it modifies the original matrix in-place
        return
