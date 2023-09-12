#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        expression = [expression]
        operators = ['+', '-', '*']
        for ope in operators:
            exp_list = []
            for e in expression:
                exp_list.extend(e.split(ope))
            expression = exp_list

        print(expression)


# @lc code=end

