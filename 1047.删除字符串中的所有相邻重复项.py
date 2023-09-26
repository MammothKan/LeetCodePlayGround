#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:

        # 栈 维护保留的字符
        stack = []
        for i in range(0, len(s)):
            if len(stack) == 0 or s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        
        return ''.join(stack)

# @lc code=end

