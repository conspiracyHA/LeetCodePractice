from typing import *


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        move_value = arr[start]
        if move_value == 0:
            return True
        been_to = {start}
        not_processed = set()
        def insert_to_not_processed(index):
            if index >= len(arr):
                return
            if index < 0:
                return
            if index in been_to:
                return
            not_processed.add(index)
            return
        insert_to_not_processed(start + move_value)
        insert_to_not_processed(start - move_value)
        while len(not_processed) != 0:
            checking = not_processed.pop()
            move_value = arr[checking]
            if move_value == 0:
                return True
            been_to.add(checking)
            insert_to_not_processed(checking + move_value)
            insert_to_not_processed(checking - move_value)
        return False


if __name__ == '__main__':
    test = [
        ([4, 2, 3, 0, 3, 1, 2], 5),
        ([4,2,3,0,3,1,2], 0,),
        ([3,0,2,1,2], 2),
    ]
    answer = [
        True, True, False
    ]
    for (t_arr, t_start), a in zip(test, answer):
        if Solution().canReach(t_arr, t_start) == a:
            print('pass')
        else:
            print('wrong answer')

