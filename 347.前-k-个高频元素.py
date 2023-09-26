#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # map()作计数器，sorted()对map进行排序，而后返回前k个
        hashtable = {}
        for n in nums:
            hashtable[n] = hashtable.get(n, 0) + 1
        # print(hashtable)

        sorted_hashtable = sorted(hashtable.items(), key=lambda x:x[1], reverse=True)
        # print(sorted_hashtable)

        result = []
        for i in range(k):
            result.append(sorted_hashtable[i][0])
        return result

# @lc code=end

