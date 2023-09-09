#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool: 
    
        # 递归 1
        # 逐次 除2 
        # 直到结果==1，说明可以被2的幂次整除，返回 True
        # 或者结果<1，出现小数，无法整除，返回False
        # def recurrence(n):
        #     if n == 1:
        #         return True
        #     elif n < 1:
        #         return False
        #     n = recurrence(n/2)
        #     return n
        
        # return recurrence(n)

        # 递归 2
        # 与 方法1 类似，不同之处在于
        # 当结果中出现小数时，便返回Flase，提早结束循环
        def recurrence(n):
            if n == 1:
                return True
            elif n == 0 or n % 1 != 0:
                return False
            n = recurrence(n/2)
            return n
        
        return recurrence(n)


# @lc code=end

