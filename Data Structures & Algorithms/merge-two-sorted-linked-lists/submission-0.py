# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        
        head = None
        curr = head

        while list1 and list2:
            node = ListNode()
            if list1.val < list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            
            if head is None:
                head = node
                curr = head
            else:
                curr.next = node
                curr = curr.next
        
        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next
        
        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next
        
        return head