#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # 三指针法
        # 存在bug，无法正确回溯sub_tail的位置
        """
        if len(s) == 1: return False

        matching = 0

        for detect_cursor in range(1, len(s)):
            # detect substring
            if matching == 0:
                sub_tail = detect_cursor
                if s[detect_cursor] == s[0]:
                    matching = 1
                    sub_tail = detect_cursor - 1
                    sub_cursor = 1 % (sub_tail+1)
                    continue
            # match substring
            if matching == 1:
                if s[detect_cursor] == s[sub_cursor]:
                    sub_cursor = (sub_cursor + 1) % (sub_tail+1)
                else:
                    if s[detect_cursor] == s[0]:
                        sub_tail = detect_cursor - 1
                    else:
                        matching = 0
                        sub_tail = detect_cursor
                    sub_cursor = 1 % (sub_tail+1)
            
            if sub_tail >= len(s)//2: return False
        
        return True if sub_cursor == 0 else False
        """

        # KMP法
        # 核心思想：一个可循环字符串中，相等的最长前缀串和后缀串不包含的子串，便是最小的重复子串
        # next数组，实则为前缀表，即s子串中相同前缀和后缀的长度
        next = [-1] * len(s)
        prefix_tail = -1
        for suffix_tail in range(1, len(s)):
            # print(f'suffix_tail={suffix_tail}')
            while prefix_tail > -1 and s[prefix_tail+1] != s[suffix_tail]:
                # prefix_tail -= 1
                prefix_tail = next[prefix_tail]
            if s[prefix_tail+1] == s[suffix_tail]:
                prefix_tail += 1
            next[suffix_tail] = prefix_tail
        # print(next)

        if next[-1] != -1 and len(s) % (len(s) - (next[-1]+1)) == 0:
            return True
        return False


# "aabaaba"
# "abaababaab"


# @lc code=end

