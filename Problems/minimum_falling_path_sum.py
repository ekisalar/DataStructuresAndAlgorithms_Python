# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row
# that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col),
# or (row + 1, col + 1).
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Example
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.

# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.

# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100


# min(min_falling_path(row+1, col-1),
#     min_falling_path(row+1, col),
#     min_falling_path(row+1, col+1))


import sys
from typing import List


class SolutionBruteForce:
    def min_falling_path_sum(self, matrix: List[List[int]]) -> int:
        min_falling_sum = sys.maxsize
        for startCol in range(len(matrix)):
            min_falling_sum = min(min_falling_sum, self.__find_min_falling_path_sum(matrix, 0, startCol))

        return min_falling_sum

    def __find_min_falling_path_sum(self, matrix: List[List[int]], row, col) -> int:

        # if col is out of the left or right boundary
        if col < 0 or col == len(matrix):
            return sys.maxsize

        # if reach the last row
        if row == len(matrix) - 1:
            return matrix[row][col]

        left = self.__find_min_falling_path_sum(matrix, row + 1, col - 1)
        middle = self.__find_min_falling_path_sum(matrix, row + 1, col)
        right = self.__find_min_falling_path_sum(matrix, row + 1, col + 1)

        return min(left, middle, right) + matrix[row][col]


class SolutionTopDownDynamic:
    testMemo: List[List[int]] = [[]]

    def min_falling_path_sum(self, matrix: List[List[int]]) -> int:
        self.testMemo[4][10] = 25
        n = len(matrix)
        memo = [[None] * n for i in range(n)]
        min_falling_sum = sys.maxsize

        for startCol in range(len(matrix)):
            min_falling_sum = min(min_falling_sum, self.__find_min_falling_path_sum(matrix, 0, startCol, memo))

        return min_falling_sum

    def __find_min_falling_path_sum(self, matrix: List[List[int]], row, col, memo: List[List[int]]) -> int:

        # if col is out of the left or right boundary
        if col < 0 or col == len(matrix):
            return sys.maxsize

        # if reach the last row
        if row == len(matrix) - 1:
            return matrix[row][col]

        if memo[row][col] is not None:
            return memo[row][col]

        left = self.__find_min_falling_path_sum(matrix, row + 1, col - 1, memo)
        middle = self.__find_min_falling_path_sum(matrix, row + 1, col, memo)
        right = self.__find_min_falling_path_sum(matrix, row + 1, col + 1, memo)

        memo[row][col] = min(left, middle, right) + matrix[row][col]
        return memo[row][col]


testCase = [[-19, 57], [-40, -5]]
solutionBruteForce = SolutionBruteForce()
print(solutionBruteForce.min_falling_path_sum(testCase))

solutionTopDownDynamic = SolutionTopDownDynamic()
print(solutionTopDownDynamic.min_falling_path_sum(testCase))
