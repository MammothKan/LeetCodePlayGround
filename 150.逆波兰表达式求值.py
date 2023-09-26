#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # 栈
        # 将tokens中的数字逐一压入栈中
        # 遇到 tokens 中的运算符时，pop两个元素做运算
        # 运算结果压入栈中
        stack = []
        for c in tokens:
            # str.isdigit() 无法探测到负整数
            # c的长度大于1，c一定不是运算符号，可能是负整数
            if len(c) > 1 or c.isdigit():
                stack.append(c)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if c == '+':
                    stack.append(a+b)
                elif c == '-':
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
                elif c == '/':
                    r = str(a/b)
                    # 向零截断
                    dot_idx = r.find('.')
                    if dot_idx != -1:
                        stack.append(r[:dot_idx])
                    else:
                        stack.append(r)
        
        return int(stack.pop())

# @lc code=end

