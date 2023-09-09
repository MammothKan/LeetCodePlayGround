#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 递归
        # 利用递归的思想，维护整个链表，从链表的最后一个元素开始处理
        def remove_node(head, val):
            # 基本案例 basic case
            # 当 节点为None时，结束递推
            if head is None:
                return head
            # 递推关系 recurrence relation
            # head.next 应该 指向已经被删除等于val节点的链表
            # 已经被删除等于val节点的链表 由return完成
            head.next = remove_node(head.next, val)
            return head.next if head.val == val else head

        return remove_node(head, val)


# @lc code=end

