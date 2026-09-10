# Definition for singly-linked list.

#Given the head of a singly linked list, 
# return true if it is a palindrome or false otherwise.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def _reverse_list(self, node: ListNode):
        head = None
        while node is not None:
            n = ListNode(node.val)
            n.next = head
            head = n
            node = node.next
        return head
    def _is_equal(self, list1, list2):
        while list1 is not None and list2 is not None:
            if list1.val != list2.val: return False
            list1 = list1.next
            list2 = list2.next
        if list1 is None and list2 is None:
            return True
        else: return False
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        reversed_list = self._reverse_list(head)
        is_equal = self._is_equal( head, reversed_list)

        return is_equal

        
    