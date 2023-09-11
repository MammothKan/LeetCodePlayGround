#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # 直接调用log function
        if n <= 0: return False
        import math
        exponential = math.ceil(math.log(n, 3))
        print(exponential)
        print(exponential % 1)

        if 3**exponential == n:
            return True
        else:
            return False
    
        # 递归
        # if n == 1: return True
        # def isEqualtoN(n, power):
        #     if power == n:
        #         return True
        #     elif power > n:
        #         return False
        #     return isEqualtoN(n, power*3)
        
        # return isEqualtoN(n=n, power=3)


# @lc code=end

