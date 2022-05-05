from typing import *


"""
Given a m * n matrix of ones and zeros,
return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        row_count = len(matrix)
        col_count = len(matrix[0])

        def is_valid_one(row, col):
            if row >= row_count:
                return False
            if col >= col_count:
                return False
            return matrix[row][col] == 1

        def check_later_value(row, col):
            nonlocal result
            side = 2
            while True:

                for plus in range(side):
                    if is_valid_one(row + plus, col + side - 1) is False:
                        return
                for plus in range(side):
                    if is_valid_one(row + side - 1, col + plus) is False:
                        return
                # print(f'{row}, {col} with side {side}')
                result += 1
                side += 1

        for i in range(row_count):
            for j in range(col_count):
                if matrix[i][j] == 1:
                    result += 1
                    check_later_value(i, j)
        return result


if __name__ == '__main__':
    test = [
        [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ],
        [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ],
    ]
    answer = [
        15,
        7
    ]
    for t, a in zip(test, answer):
        if Solution().countSquares(t) == a:
            print('pass')
        else:
            print('wrong answer')