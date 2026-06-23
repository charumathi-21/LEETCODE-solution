class Solution(object):
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            # Top row
            result += matrix.pop(0)

            # Right column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Bottom row
            if matrix:
                result += matrix.pop()[::-1]

            # Left column
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result