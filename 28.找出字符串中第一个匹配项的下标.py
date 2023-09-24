#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力匹配 
        # 时间复杂度O(n*m)，n为haystack的长度，m为needle的长度
        """
        for i in range(len(haystack)):
            _i = i  # 记录从haystack开始匹配的位置
            for j in range(len(needle)):
                # 从 _i 开始，逐一匹配needle中的字符
                if  _i < len(haystack) and haystack[_i] == needle[j]:
                    _i += 1
                    if j == len(needle)-1: return i     # 若成功匹配到needle单词的最后一个字符，返回开始匹配的下表 i
                else:
                    break   # 一旦匹配不超过，从haystack的下一个字符开始重新匹配
        return -1
        """
    
        # KMP算法
        

# @lc code=end

