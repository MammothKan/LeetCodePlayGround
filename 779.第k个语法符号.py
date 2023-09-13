#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # 递归法 对第n行第k个元素的生成过程进行溯源
        # based on the rule of 0->01 and 1->10,
        # when the remainder of k % 2 equals to 0, the element unchanges,
        # while the remainder of k % 2 equals to 1, the element needs to be negated (取反)
        def tracert(n, k):
            if n == 1:
                return False
            else:
                return tracert(n-1, k // 2) if k % 2 == 0 else ~tracert(n-1, k // 2)
            
        return 1 if tracert(n, k-1) else 0

# @lc code=end

