# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        pointer = dummy_node

        left, right = list1, list2

        while left and right:
            if left.val > right.val:
                dummy_node.next = right
                right = right.next
            else:
                dummy_node.next = left
                left = left.next
            dummy_node = dummy_node.next
        
        if left or right:
            dummy_node.next = left if left else right
        
        return pointer.next
