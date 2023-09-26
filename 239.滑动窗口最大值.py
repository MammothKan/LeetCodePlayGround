#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # 方法一：
        # 用一个队列来模拟大小为k的窗口的滑动
        # max_e 维护当前队列中的最大值
        # 窗口向右滑动时，分别对队列进行pop和push操作，并更新max_e
        # 减枝操作：当新push的值不大于max_e，且pop出去的值非max_e，max_e无需更新
        # 此方法的时间复杂度为O(n*k), n为数组nums的长度，k为滑动窗口的大小
        # 在leetcode中会timeout，无论用 list() 或 collection.deque() 做队列
        # 写法1:用list()做队列
        """
        import copy
        k_queue = copy.copy(nums[:k])
        max_e = max(k_queue)
        k_max = []
        k_max.append(max_e)
        for i in range(k, len(nums)):
            pop_e = k_queue.pop(0)
            # print(f'pop_e={pop_e}')
            k_queue.append(nums[i])
            # print(k_list)
            if max_e < nums[i]:      # 新push的数大于max_e
                max_e = nums[i]      # max_e被更新为push_e
            elif max_e == pop_e:     # 新push的数不大于max_e 且max_e被pop
                max_e = max(k_queue) # 重新查找最值更新max_e
            k_max.append(max_e)
            # print(f'max_e={max_e}')
        return k_max
        """
        # 写法2:用queue()做队列
        """
        import collections
        k_queue = collections.deque()
        for i in range(k):
            k_queue.append(nums[i])
        max_e = max(k_queue)
        k_max = []
        k_max.append(max_e)
        for i in range(k, len(nums)):
            pop_e = k_queue.popleft()
            # print(f'pop_e={pop_e}')
            k_queue.append(nums[i])
            # print(k_list)
            if max_e < nums[i]:      # 新push的数大于max_e
                max_e = nums[i]      # max_e被更新为push_e
            elif max_e == pop_e:     # 新push的数不大于max_e 且max_e被pop
                max_e = max(k_queue) # 重新查找最值更新max_e
            k_max.append(max_e)
            # print(f'max_e={max_e}')
        return k_max
        """

        # 方法二：
        # 单调队列
        # 与方法一相比，此方法的队列是一个单调递减队列
        # 在窗口滑动过程中，更新队列只保存k个范围内大于等于新push数的数
        # 这保证单调队列的第0个数，始终是子数组的最大值
        # 写法1: 用 list() 作队列
        # list.pop(0)的时间复杂度为O(n)，会timeout
        """
        decreasing_queue = []
        last_element = 100000  # decreasing_list中的最小值
        result = []
        for in_idx, in_num in enumerate(nums):
            # pop
            # 如果单调队列的第0个数，等于滑动窗口被移除的数，则pop
            out_idx = max(in_idx - k, -1)
            if out_idx > -1 and nums[out_idx] == decreasing_queue[0]:
                decreasing_queue.pop(0)
            # push
            # 如果新push的数，小于等于单调队列的最后一个数，直接push
            # 如果新push的数，大于单调队列的最后一个数，循环的此队列，
            # 按原排序只保留大于等于新push数的数，最后再将新push的数从尾部push
            if in_num > last_element:
                # 按原排序循环单调队列
                for i in range(len(decreasing_queue)):
                    e = decreasing_queue.pop(0)              # 从头部pop
                    if e >= in_num:
                        decreasing_queue.append(e)           # 大于等于的，重新从尾部push
            decreasing_queue.append(in_num)                  # 从尾部push新的数
            last_element = in_num
            if in_idx >= k-1: result.append(decreasing_queue[0])
        return result
        """
        # 写法2: 用 collection.deque() 作队列
        # deque.popleft()替换list.pop(0)
        import collections
        decreasing_queue = collections.deque()
        last_element = 100000  # decreasing_list中的最小值
        result = []
        for in_idx, in_num in enumerate(nums):
            # pop
            # 如果单调队列的第0个数，等于滑动窗口被移除的数，则pop
            out_idx = max(in_idx - k, -1)
            if out_idx > -1 and nums[out_idx] == decreasing_queue[0]:
                decreasing_queue.popleft()
            # push
            # 如果新push的数，小于等于单调队列的最后一个数，直接push
            # 如果新push的数，大于单调队列的最后一个数，循环的此队列，
            # 按原排序只保留大于等于新push数的数，最后再将新push的数从尾部push
            if in_num > last_element:
                # 按原排序循环单调队列
                for i in range(len(decreasing_queue)):
                    e = decreasing_queue.popleft()           # 从头部pop
                    if e >= in_num:
                        decreasing_queue.append(e)           # 大于等于的，重新从尾部push
            decreasing_queue.append(in_num)                  # 从尾部push新的数
            last_element = in_num
            if in_idx >= k-1: result.append(decreasing_queue[0])
        return result

# @lc code=end

