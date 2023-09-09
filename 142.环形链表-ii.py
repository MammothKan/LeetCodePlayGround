#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 哈希表法
        #   在遍历链表的过场中，借助一个哈希表，记录已经遍历的node
        #   通过查找哈希表可以快速确定 next node 是否在之前出现过
        if head == None:
            return None
        hashmap = {head:0}
        p = head
        p_idx = 0
        while p.next is not None:
            p = p.next
            p_idx += 1
            if hashmap.get(p, -1) == -1:
                hashmap[p] = p_idx
            else:
                return p
        return None


# @lc code=end

