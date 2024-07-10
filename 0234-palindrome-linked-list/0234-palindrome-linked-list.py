# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left, right = head, head
        array = []

        while right is not None:
            array.append(right.val)
            right = right.next

        for i in range(len(array) - 1, -1, -1):
            if array[i] != left.val:
                return False
            
            array.pop()
            left = left.next

        return True
