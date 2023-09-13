#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        
        # 采用 栈 来维护中括号之间的关系 []
        #   1. 将 str 中的字符逐个压入栈中；
        #   2. 当 字符为 "]" 时，从栈中弹出字符，获得编码字符串encoded_string和重复次数k；
        #   3. 将k与encoded_string相乘获得decoded_string，而后将decoded_string逐个压入栈中；
        #   4. 重复第1步，直到所有str中的字符都被压入栈中。
        stack = []

        for char in s:
            #   1. 将 str 中的字符逐个压入栈中；
            if char != ']':
                stack.append(char)
            #   2. 当 字符为 "]" 时，从栈中弹出字符
            else:
                # 获得编码字符串encoded_string
                encoded_string = ''
                while True:
                    c = stack.pop()
                    if c == '[':
                        break
                    else:
                        encoded_string = c + encoded_string
                # 重复次数k
                k = ''
                while True:
                    if len(stack) > 0 and stack[-1].isdigit():
                        k = stack.pop() + k
                    else:
                        break
                k = int(k)
                #   3. 将k与encoded_string相乘获得decoded_string，而后将decoded_string逐个压入栈中；
                decoded_string = encoded_string * k
                for char in decoded_string:
                    stack.append(char)
        
        decoded_string = ''.join(stack)
        return decoded_string

# @lc code=end

