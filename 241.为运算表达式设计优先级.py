#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def calculation_unit(a, b, ope):
            if ope == '+':
                return a + b
            elif ope == '-':
                return a - b
            else:
                return a * b

        elements, operators = [], []
        for i in range(len(expression)):
            if expression[i].isdigit():
                element_from = i
            else:
                element_to = i
                elements.append(int(expression[element_from: element_to]))
                operators.append(expression[i])
        elements.append(int(expression[element_from: ]))
        
        # print(elements)
        # print(operators)

        def f(n):
            ope_idx = n-1     # index of the operators
            if n == 0:
                return [elements[0]]
            if n == 1:
                return [calculation_unit(a = elements[0], b=elements[1], ope=operators[ope_idx])]
            results = []

            for pre_result in f(n-1):
                results.append(calculation_unit(a=pre_result, b=elements[n], ope=operators[ope_idx]))
            last_pair = calculation_unit(a=elements[n-1], b=elements[n], ope=operators[ope_idx])
            print(last_pair)
            for pre_result in f(n-2):
                results.append(calculation_unit(a=pre_result, b=last_pair, ope=operators[ope_idx-1]))
            return results

        return f(n=len(elements)-1)


# @lc code=end

