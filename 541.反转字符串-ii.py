#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        # 模拟交换的过程
        # 1. 查找并遍历的每个长度2k的字符串片段
        # 2. 交换字符串片段中的前k个字符

        def reverse(left, right):
            part_str = ''
            mid = min((left + k - 1), right)    # 交换前k个字符
            for i in range(mid, left-1, -1):
                part_str += s[i]
            for i in range(mid+1, right+1):
                part_str += s[i]
            return part_str
        
        revStr = ''
        if len(s) <= 2*k:
            revStr += reverse(left=0, right=len(s)-1)
        else:
            # 查找并遍历的每个长度2k的字符串片段
            for i in range(0, len(s)-2*k, 2*k):
                revStr += reverse(left=i, right=i+2*k-1)
            revStr += reverse(left=i+2*k, right=len(s)-1)

        return revStr

# @lc code=end

