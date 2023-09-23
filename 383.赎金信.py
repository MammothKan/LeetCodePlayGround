#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # 哈希冲撞法
        # 此处采用数组而不是map来作为哈希表的基础数据结构
        # 因为此题中的字母只有26个，数量固定吗，因此可以使用数组来维护哈希表
        # 数组的索引 理论上比 map更快

        hashdict = [0] * 26
        for c in magazine:
            hashdict[ord(c) - ord('a')] += 1

        for c in ransomNote:
            hashdict[ord(c) - ord('a')] -= 1
        
        for count in hashdict:
            if count < 0:
                return False
        
        return True

# @lc code=end

