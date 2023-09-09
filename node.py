from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @staticmethod
    def printListNode(listNodes: Optional[ListNode]):
        _list = list()
        while listNodes is not None:
            _list.append(listNodes.val)
            listNodes = listNodes.next
        return _list

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode(val=-1)
        dummy.next = head

        _current_pointer = dummy
        current_pointer = head
        _slot_pointer = dummy

        flag = 0
        while current_pointer is not None:
            if flag == 0:
                if current_pointer.val < x:
                    _slot_pointer = _slot_pointer.next
                    current_pointer = current_pointer.next
                    _current_pointer = _current_pointer.next
                else:
                    flag = 1
                    current_pointer = current_pointer.next
                    _current_pointer = _current_pointer.next
            
            else:
                if current_pointer.val < x:
                    _current_pointer.next = current_pointer.next
                    next_pointer = current_pointer.next
                    
                    current_pointer.next = _slot_pointer.next
                    _slot_pointer.next = current_pointer
                    _slot_pointer = _slot_pointer.next
                    current_pointer = next_pointer
                    #_current_pointer = _current_pointer.next
                else:
                    current_pointer = current_pointer.next
                    _current_pointer = _current_pointer.next
        
        return dummy.next


if __name__ == '__main__':
    l1 = []
    x = 2
    # l2 = [1,2,4]

    l1_head = ListNode(val=l1[0])
    # l2_head = ListNode(val=l2[0])

    l1_pointer = l1_head
    # l2_pointer = l2_head

    for i in range(1, len(l1)):
        l1_pointer.next = ListNode(val=l1[i])
        l1_pointer = l1_pointer.next

    # for i in range(1, len(l2)):
    #     l2_pointer.next = ListNode(val=l2[i])
    #     l2_pointer = l2_pointer.next

    # print('l2 start')
    # head = l2_head
    # _list = list()
    # while head is not None:
    #     _list.append(head.val)
    #     head = head.next
    # print(_list)
    # print('l2 end')
    

    result = Solution().partition(head=l1_head, x=x)

    result_list = list()
    while result is not None:
        result_list.append(result.val)
        result = result.next

    print(result_list)
    print('over')


