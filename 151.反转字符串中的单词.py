#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        # 双指针法探测每个单词的左右边界
        left, right = [], []
        for i, c in enumerate(s):
            if (i == 0 and c != ' ') or (i>0 and s[i-1] == ' ' and c != ' '):
                left.append(i)
            if (i > 0 and s[i-1] != ' ' and c == ' '):
                right.append(i)
            if c != ' ' and i == len(s)-1:
                right.append(i+1)

        assert len(left) == len(right)
        # 从尾部开始遍历left和right，实现反转字符串中单词顺序的目的
        res = []
        for i in range(len(left)-1, -1, -1):
            res.append(s[left[i]:right[i]])
        
        return ' '.join(res)

# @lc code=end

