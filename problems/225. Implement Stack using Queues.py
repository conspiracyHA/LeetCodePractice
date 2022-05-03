class MyStack:

    def __init__(self):
        self._arr = list()

    def push(self, x: int) -> None:
        self._arr.append(x)

    def pop(self) -> int:
        *self._arr, result = self._arr
        return result

    def top(self) -> int:
        return self._arr[-1]

    def empty(self) -> bool:
        return len(self._arr) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()