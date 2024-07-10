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

        while array:
            if len(array) == 1:
                return True
            if array.pop(0) != array.pop():
                return False

        return True
