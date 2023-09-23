#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        # 哈希冲撞法
        # 注意题干中的 “无限循环” 字样
        # 可以通过判断是否开始循环来判断
        
        # 将一个正整数按位数拆分为多个只有一位的正整数
        import numpy as np
        def divideint(n) -> list:
            int_list = []
            while n > 0:
                int_list.append(n % 10)
                n = n // 10
            int_list.reverse()
            # return int_list
            return np.array(int_list)
        
        hashtable = {}
        hashtable[n] = 0
        while True:
            int_list = divideint(n)
            n = np.sum(np.power(int_list, 2))   # 每一次将该数替换为它每个位置上的数字的平方和
            if n not in hashtable:              # 哈希冲撞 一旦冲撞发生 即开始无限循环
                hashtable[n] = 0
            else:
                break
        
        if n == 1:
            return True
        else:
            return False
            
# @lc code=end

