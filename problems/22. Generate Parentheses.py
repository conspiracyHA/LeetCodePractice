"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

"""
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current = {'()'}
        for i in range(n - 1):
            next = set()
            for tmp in current:
                for j in range(len(tmp)):
                    next.add(tmp[:j] + '()' + tmp[j:])
            current = next
        return current


if __name__ == '__main__':
    test = 3
    answer = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    print(
        Solution().generateParenthesis(test) == answer
    )