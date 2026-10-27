class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        #how do I transpose a matrix?
        rows = len(matrix)
        cols = len(matrix[0])

        result = []

        for i in range(cols):
            result.append([0] * rows) # nice way of creating a matrix to store the new format

        for i in range(cols):
            for j in range(rows):
                result[i][j] = matrix[j][i] 

        return result