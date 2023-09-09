#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        sort_pool = list()
        for LN in lists:
            p = LN
            while p is not None:
                sort_pool.append(p)
                p = p.next
        sort_pool.sort(key=lambda node: node.val)

        dummy = ListNode(val=-1)
        pointer = dummy
        for node in sort_pool:
            pointer.next = node
            pointer = pointer.next
        pointer.next = None

        return dummy.next

# @lc code=end

