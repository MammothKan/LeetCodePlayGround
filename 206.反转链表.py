#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 头插法
        # 新建一个链表头
        # 遍历input列表，将每个node从新建链表头部插入
        new_head = ListNode(val=0, next=None)
        curr_pointer = head
        while curr_pointer is not None:
            next_pointer = curr_pointer.next

            new_subhead = new_head.next
            new_head.next = curr_pointer
            curr_pointer.next = new_subhead

            curr_pointer = next_pointer
        
        return new_head.next

# @lc code=end

