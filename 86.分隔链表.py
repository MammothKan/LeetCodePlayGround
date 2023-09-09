#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 设置 虚拟节点
        dummy = ListNode(val=-1)
        dummy.next = head
        
        pre_current_pointer = dummy     # 当前节点的前一个节点指针
        current_pointer = head          # 当前节点指针
        _slot_pointer = dummy           # 待插入槽位（节点）指针 【插入在该节点之后】

        flag = 0
        while current_pointer is not None:

            if flag == 0:
                if current_pointer.val < x:
                    _slot_pointer = _slot_pointer.next
                    current_pointer = current_pointer.next
                    pre_current_pointer = pre_current_pointer.next
                else:
                    flag = 1
                    current_pointer = current_pointer.next
                    pre_current_pointer = pre_current_pointer.next
            else:
                if current_pointer.val < x:
                    pre_current_pointer.next = current_pointer.next
                    next_pointer = current_pointer.next
                    
                    current_pointer.next = _slot_pointer.next
                    _slot_pointer.next = current_pointer
                    _slot_pointer = _slot_pointer.next
                    current_pointer = next_pointer
                else:
                    current_pointer = current_pointer.next
                    pre_current_pointer = pre_current_pointer.next
        
        return dummy.next



# @lc code=end

