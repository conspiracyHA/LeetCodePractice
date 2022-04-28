"""
https://leetcode.com/problems/elimination-game/
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

    Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
    Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
    Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer n, return the last number that remains in arr.
"""


class Solution_:
    def lastRemaining(self, n: int) -> int:
        arr = [i for i in range(1, n + 1)]

        while len(arr) != 1:
            arr = self._first_action(arr)
            if len(arr) == 1:
                return arr[0]
            arr = self._second_action(arr)
        return arr[0]

    def _first_action(self, arr):
        killed = arr[0::2]
        print(f'first {killed}')
        return arr[1::2]

    def _second_action(self, arr):
        killed = arr[-1::-2]
        killed.reverse()
        print(f'second {killed}')
        return arr[-2::-2][::-1]


class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n, is_first_move):
            print(n, is_first_move)
            if n == 1:
                return 1
            if is_first_move:
                # [1, 2, 3, 4, 5] => [2, 4] = 2 * [1, 2]
                return 2 * helper(n//2, False)
            if n % 2 == 1:
                # [1, 2, 3, 4, 5] => [2, 4] = 2 * [1, 2]
                return 2 * helper(n // 2, True)
            # [1, 2, 3, 4] => [1, 3] = 2 * [1, 2] - 1 (都減1的意思)
            return 2 * helper(n // 2, True) - 1
        return helper(n, True)


if __name__ == '__main__':
    test = [9, 1, 8]
    answer = [6, 1, 6]
    for t, a in zip(test, answer):
        if Solution().lastRemaining(t) == a:
            print('pass')
        else:
            print('wrong answer')
    # for i in range(15,35):
    #     print(f'{i}'.center(20, '-'))
    #     Solution_().lastRemaining(i)




