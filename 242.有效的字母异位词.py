#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 将 字符串s 转换为一个记录字符及字符数量的哈希表
        hashtable = {}
        for c in s:
            if c not in hashtable:
                hashtable[c] = 1
            else:
                hashtable[c] += 1
        
        # 根据 字符串c 逐个函数哈斯表中的字符
        for c in t:
            if c in hashtable:
                hashtable[c] -= 1
                if hashtable[c] == 0:
                    hashtable.pop(c)    # 当字符数量为0时，从哈希表中删除该字符
            else:
                return False            # 当字符串c中存在无法从哈斯表中检索到的字符，则返回False
        
        if len(hashtable) == 0:
            return True
        else:
            return False
        
# @lc code=end

