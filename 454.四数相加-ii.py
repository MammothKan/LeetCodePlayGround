#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # 暴力搜索法 时间复杂度O(n^4)
        # 将4个数组分为两组，借助hashtable保存 (nums1+nums2) 的结果，而后查找 -(nums3+nums4) 的匹配结果，此法的时间复杂度为 O(2 * n^2)
        hashtable = {}
        for n1 in nums1:
            for n2 in nums2:
                hashtable[(n1+n2)] = hashtable.get((n1+n2), 0) + 1
        
        resules = 0
        for n3 in nums3:
            for n4 in nums4:
                resules += hashtable.get(-(n3+n4), 0)
        
        return resules
# @lc code=end

