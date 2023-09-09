#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None:
            return head

        dummy = ListNode(val=-1)
        dummy.next = head

        pre_n_pointer = None
        n_pointer = None
        pointer = head

        interval_len = 0
        while interval_len != n:
            interval_len += 1
            pointer = pointer.next
        
        pre_n_pointer = dummy
        n_pointer = head

        while pointer is not None:
            pre_n_pointer = pre_n_pointer.next
            n_pointer = n_pointer.next
            pointer = pointer.next

        pre_n_pointer.next = n_pointer.next

        return dummy.next




        # if head == None:
        #     return head

        # dummy = ListNode(val=-1)
        # dummy.next = head
        # pre_current_pointer = dummy
        # current_pointer = head

        # # 第一遍 遍历List 获取链表长度
        # len = 0
        # while current_pointer is not None:
        #     len += 1
        #     current_pointer = current_pointer.next

        # # 第二遍 遍历list 删除第 (len-n) 个节点
        # current_pointer = head
        # for i in range(0, len-n):
        #     pre_current_pointer = pre_current_pointer.next
        #     current_pointer = current_pointer.next

        # pre_current_pointer.next = current_pointer.next

        # return dummy.next

            

# @lc code=end

