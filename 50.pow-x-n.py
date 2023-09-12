#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        # 快速幂 + 递归
        # 逐次对幂次 n 整除 2，x变为x^2，以此来降低幂运算的次数
        # 对于幂次 n 无法被 2 整除的情况下，x变为x^2 * x
        if x == 0 or x == 1: 
            return x
        if n == 0:
            return 1
        
        def divideN(x, n):
            if n == 1:
                return x
            if n % 2 == 1:
                remainder = x
            else:
                remainder = 1
            return divideN(x*x, n // 2) * remainder
        
        result = divideN(x, n) if n>0 else 1/divideN(x, -n)
        return result

# @lc code=end

