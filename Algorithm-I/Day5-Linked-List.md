## 876. Middle of the Linked List
### Question
Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
### Notes
- Two pointers: the fast pointer goes twice as fast as the slow pointer.
- Why check `fast.next`? If `fast.next = None`, `fast.next.next` will cause error.
### Solution
``` 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```


## 19. Remove Nth Node From End of List
### Question
Given the head of a linked list, remove the nth node from the end of the list and return its head.
### Notes
- [Reference](https://github.com/qilinz/Leetcode-Practice/blob/main/Study-Plan/Algorithm/Algorithm-I/Day2-5-two-pointers.md)
- Why head is modified: slow is a reference of head, not a copy of head. Thus, if slow is changed, head is affected as well. ("you are modifying a child node that the head is pointing to")
### Solution
``` 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # make fast is n ahead of slow
        for _ in range(n):
            fast = fast.next

        # Hold exception:
        # if fast is none, it means fast reach "the next of the last node". 
        # This means n = the length of the linked list. 
        # n^th node from the end is the first node of the linked list.
        if fast is None:
            return head.next

        # make the fast goes to the end
        # then the slow will be one node before the target node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
```