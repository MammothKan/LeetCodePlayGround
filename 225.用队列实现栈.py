#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    # 单队列实现法
    # 从头部弹出的元素从尾部重新压入
    def __init__(self):
       self.list = []


    def push(self, x: int) -> None:
        self.list.append(x)


    def pop(self) -> int:
        for i in range(len(self.list)-1):
            self.list.append(self.list.pop(0))
        return self.list.pop(0)
        

    def top(self) -> int:
        for i in range(len(self.list)-1):
            self.list.append(self.list.pop(0))
        e = self.list[0]
        self.list.append(self.list.pop(0))
        return e


    def empty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False


    """
    # 双队列实现法
    def __init__(self):
       # 主队列和备份队列同级别
       # 主队列和备份队列必有一个为空
       self.list = []   # 主队列
       self._list = []  # 备份队列


    def push(self, x: int) -> None:
        if len(self.list) != 0:
            self.list.append(x)
        else:
            self._list.append(x)



    def pop(self) -> int:
        if len(self.list) != 0:
            while len(self.list) != 1:
                self._list.append(self.list.pop(0))
            return self.list.pop(0)
        else:
            while len(self._list) != 1:
                self.list.append(self._list.pop(0))
            return self._list.pop(0)
        

    def top(self) -> int:
        if len(self.list) != 0:
            while len(self.list) != 1:
                self._list.append(self.list.pop(0))
            e = self.list[0]
            self._list.append(self.list.pop(0))
        else:
            while len(self._list) != 1:
                self.list.append(self._list.pop(0))
            e = self._list[0]
            self.list.append(self._list.pop(0))
        return e


    def empty(self) -> bool:
        if len(self.list) + len(self._list) == 0:
            return True
        return False
    """


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

