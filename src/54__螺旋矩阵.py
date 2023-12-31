from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []  # Initialize an empty list to store the spiral order of elements
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Directions: right, down, left, up
        dir = 0  # Current direction index
        x = 0  # Current row index
        y = 0  # Current column index
        
        # Iterate over each element in the matrix
        for _ in range(len(matrix) * len(matrix[0])):
            ans.append(matrix[x][y])  # Add the current element to the answer list
            matrix[x][y] = 0x3f3f3f3f  # Mark the current element as visited
            
            # Calculate the next potential position
            nx = x + d[dir][0]
            ny = y + d[dir][1]
            
            # Check if the next position is out of bounds or already visited
            if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])) or matrix[nx][ny] == 0x3f3f3f3f:
                dir = (dir + 1) % 4  # Change direction (right -> down -> left -> up)
                nx = x + d[dir][0]  # Recalculate the next position after changing direction
                ny = y + d[dir][1]
            
            x = nx  # Update the current row index with the new position
            y = ny  # Update the current column index with the new position
        
        return ans  # Return the spiral order of elements
