#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:

        # 递归（动归）
        def f(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return f(n-1) + f(n-2)
        
        return f(n)


# @lc code=end

