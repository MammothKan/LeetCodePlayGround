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
        element_from, element_to = -1, -1
        for i in range(len(expression)):
            if expression[i].isdigit():
                element_from = i if element_from == -1 else element_from
            else:
                element_to = i
                elements.append(int(expression[element_from: element_to]))
                element_from, element_to = -1, -1
                operators.append(expression[i])
        elements.append(int(expression[element_from: ]))
        
        # print(elements)
        # print(operators)

        def f(n, elements, operators):
            if n == 0:
                return [elements[0]]
            if n == 1:
                return [calculation_unit(a = elements[0], b=elements[1], ope=operators[0])]
            
            results = []
            for ele_idx in range(1, n+1):
                ope_idx = ele_idx-1     # index of the operators

                # 将 expression 以 ope_main 为中心分为两个部分left和right
                ele_left, ele_right = elements[:ele_idx], elements[ele_idx:]
                ope_left, ope_right = operators[:ope_idx], operators[ope_idx:]
                ope_main = ope_right[0]
                ope_right.pop(0)
                # 采用递归法，分别求解left和right expression的所有计算结果
                results_left = f(n=len(ele_left)-1, elements=ele_left, operators=ope_left)
                results_right = f(n=len(ele_right)-1, elements=ele_right, operators=ope_right)
                # 遍历left和right expression的results，用ope_main做运算，获得最后结果
                for l in results_left:
                    for r in results_right:
                        results.append(calculation_unit(a=l, b=r, ope=ope_main))
            return results
        
        return f(n=len(elements)-1, elements=elements, operators=operators)

# @lc code=end

