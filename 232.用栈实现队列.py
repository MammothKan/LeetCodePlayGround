#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        # 若输出栈（stack_out）非空，将输入栈（stack_in）中的所有元素pop后，
        # push入stack_out中，然后从stack_out中pop一个元素
        # 若stack_out非空，直接从stack_out中pop一个元素
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


    def peek(self) -> int:
        # 与pop()同理
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


    def empty(self) -> bool:
        if len(self.stack_in) + len(self.stack_out) == 0:
            return True
        return False

    """
    def __init__(self):
        self.stack = []
        self.stack_bucket = []


    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        while len(self.stack) != 0:
            self.stack_bucket.append(self.stack.pop())
        e = self.stack_bucket.pop()
        while len(self.stack_bucket) != 0:
            self.stack.append(self.stack_bucket.pop())
        return e


    def peek(self) -> int:
        while len(self.stack) != 0:
            e = self.stack.pop()
            self.stack_bucket.append(e)
        while len(self.stack_bucket) != 0:
            self.stack.append(self.stack_bucket.pop())
        return e


    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
    """



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

