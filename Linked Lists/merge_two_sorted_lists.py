# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

def mergeTwoLists(self, list1: list, list2: list) ->list:
        dummy = ListNode(0)
        actual = dummy

        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                #primeira lista eh menor
                actual.next = pointer1
                pointer1 = pointer1.next
            else:
                actual.next = pointer2
                pointer2 = pointer2.next

            actual = actual.next
        if pointer1:
            actual.next = pointer1
        else:
            actual.next = pointer2

        return dummy.next #pq o primeiro no, setei como zero
