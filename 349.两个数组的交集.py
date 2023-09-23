#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 哈希表法
        # 用 nums1 构建哈希表；用 nums2 逐一删除哈希表
        intersection_set = []
        hashtable = {}
        for e in nums1:
            hashtable[e] = 1
        for e in nums2:
            if e in hashtable:
                hashtable.pop(e)
                intersection_set.append(e)
        return intersection_set

# @lc code=end

