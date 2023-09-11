#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # 递归  式除法
        # 不断对 n 做 除4 操作
        # 直到 n=1 时，说明 n 是 4 的幂
        # 或者 n 不再能被 4 整除说明 n 不是 4 的幂
        if n == 0: return False
        def tryDivision(n):

            if n==1:
                return True
            elif n % 4 == 0:
                return tryDivision(n / 4.0)
            else:
                return False
        
        return tryDivision(n)



# @lc code=end

