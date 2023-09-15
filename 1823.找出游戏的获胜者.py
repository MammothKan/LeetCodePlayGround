#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#
# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        step = 0
        bucket = dict()
        while True:
            step = (step + k) % n

            while not step in bucket.keys():
                bucket[step] = 1

            if len(bucket.keys()) == n:
                break
        
        return step+1
            



        
        # # 构建一个包含n个nodes的循环链表，每走k步删除一个node
        # # 直到链表中只省一个node时，返回结果
        # class ListNode:
        #     def __init__(self, x, next=None) -> None:
        #         self.val = x
        #         self.next = next
            
        # def pop(pre_node, deleted_node):
        #     pre_node.next = deleted_node.next
        #     return pre_node.next

        # def printListNode(head):
        #     p = head
        #     while p.next != head:
        #         print(p.val)
        #         p = p.next
        #     print(p.val)
            
        # # create a list containing n nodes from 1 to n
        # head = ListNode(x=1)
        # p = head
        # for i in range(2, n+1):
        #     p.next = ListNode(x=i)
        #     p = p.next
        # p.next = head   # 循环链表
        # pre_head = p

        # step = 1
        # while pre_head != head:
        #     # print(f'pre_head: {pre_head.val}')
        #     if step == k:
        #         # 弹出 head 执行的当前节点，并返回当前节点的下一个节点作为head
        #         head = pop(pre_node=pre_head, deleted_node=head)
        #         step = 1        # reset step variable
        #         continue
        #     pre_head = pre_head.next
        #     head = head.next
        #     step += 1
            
        # return head.val


# @lc code=end

