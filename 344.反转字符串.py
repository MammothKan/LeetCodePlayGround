#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 左右指针，从数组两端逐渐向中心逼近，交换左右指针所指的内容
        # 写法一
        """
        for i in range(len(s)//2):
            _c = s[len(s)-1-i]
            s[len(s)-1-i] = s[i]
            s[i] = _c
        """

        # 写法二
        left = 0
        right = len(s)-1
        while left < right:
            # _c = s[right]
            # s[right] = s[left]
            # s[left] = _c
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        
# @lc code=end

