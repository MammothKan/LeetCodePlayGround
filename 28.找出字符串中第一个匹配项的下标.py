#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力匹配 BurstForce
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
        # next数组，实则为前缀表，即needle子串中相同前缀和后缀的长度
        next = [-1] * len(needle)
        prefix_tail = -1
        for suffix_tail in range(1, len(needle)):
            # print(f'suffix_tail={suffix_tail}')
            while prefix_tail > -1 and needle[prefix_tail+1] != needle[suffix_tail]:
                # prefix_tail -= 1
                prefix_tail = next[prefix_tail]
            if needle[prefix_tail+1] == needle[suffix_tail]:
                prefix_tail += 1
            next[suffix_tail] = prefix_tail
        # print(next)

        i, j = -1, -1
        while i < len(haystack)-1:
            # while j < len(needle):
            if haystack[i+1] == needle[j+1]:
                # i, j += 1, 1
                i += 1
                j += 1
            else:
                if j == -1: i += 1
                else: j = next[j]
            if j == len(needle)-1:
                return i - j
        return -1


  #  "leetcode"\n"leeto"      
  # "aabaaabaaac"\n"aabaaac"
  # "adcadcaddcadde"\n"adcadde"


        

# @lc code=end

