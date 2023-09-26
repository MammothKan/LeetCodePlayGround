#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        # 用于存放左括号的栈 '(','[','{'
        left_stack = []
        for c in s:
            if c in ['(', '{', '[']:
                left_stack.append(c)
            else:
                if len(left_stack) == 0:
                    return False
                elif c == ')' and left_stack.pop() != '(':
                    return False
                elif c == ']' and left_stack.pop() != '[':
                    return False
                elif c == '}' and left_stack.pop() != '{':
                    return False
        
        return True if len(left_stack) == 0 else False

# @lc code=end

