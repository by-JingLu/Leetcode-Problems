## 237 Delete Node in a Linked List
### Notes
- A little bit easy, not a typical linked list problem
### Solution
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## 203 Remove Linked List Elements
### Question
Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.
### Notes
- Edge case: check the head value first
- Why head is modified: temp is a reference of head, not a copy of head. Thus, if temp is changed, head is affected as well. ("you are modifying a child node that the head is pointing to")
- Use `dummy` point to solve edge case: `dummy.next == head`
### Solution
Original
```
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # Edge case
        while head and head.val == val:
            head = head.next

        temp = head
        while head and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
```
Dummy
```
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        temp = dummy
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return dummy.next
```

## 19. Remove Nth Node From End of List
### Question
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
### Notes
- [Reference](https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/1164542/JS-Python-Java-C++-or-Easy-Two-Pointer-Solution-w-Explanation/)
- Edge case: n == len(linkedlist), head should be removed.
### Solution
``` 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        # make fast is n ahead of slow
        while n > 0:
            fast = fast.next
            n -= 1

        # Edge case
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

## 206 Reverse Linked List
### Question
Given the `head` of a singly linked list, reverse the list, and return the reversed list.
### Notes
- [Reference](https://www.youtube.com/watch?v=G0_I-ZF0S38)
- Use two pointers `pre` and `cur`, iterate the linked  
    ![](/Top-Interview-Easy/image/206.png)
### Solution
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = pre
            pre = cur
            cur = cur.next
            pre.next = temp
            
        return pre
```


## 21 Merge Two Sorted Lists
### Question
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
### Notes
- Use `head` to create new linked list and `tail` to loop through
- Edge case: one linked list have nodes left
### Solution
```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        # Edge case
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return head.next
```


## 234 Palindrome Linked List
### Question
Given the `head` of a singly linked list, return `true` if it is a 
palindrome or `false` otherwise.
### Notes
- Palindrom linked list -> Palindrom list/string
### Solution
```
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        left = 0
        right = len(temp) - 1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True
```

## 141 Linked List Cycle
### Question
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
### Notes
- Dictionary: it is easy, check if key exists
- Two pointer: it is math problom, if it has a circle, fast will meet slow afer `(n - pos`)` times move
### Solution
Dictionary: space, time O(n)
```
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_dict = {}
        while head:
           if head in nodes_dict:
               return True

           nodes_dict[head] = 0
           head = head.next
        return False
```
Two pointer: Now extra space, time O(n)
```
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
    
        return False
```



