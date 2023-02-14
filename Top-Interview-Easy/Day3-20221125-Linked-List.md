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
- use a dummy linked list to handle the situation: first element alse need to remove
- if use `cur.next.next`, should give the condition: `cur.next != None`
- Why head is modified: temp is a reference of head, not a copy of head. Thus, if temp is changed, head is affected as well. ("you are modifying a child node that the head is pointing to")
### Solution
Dummy
```
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
```

## 19. Remove Nth Node From End of List
### Question
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
### Notes
- [Reference](https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/1164542/JS-Python-Java-C++-or-Easy-Two-Pointer-Solution-w-Explanation/)
- Edge case: nth Node is the first node
- fast pointer reached th last node of the linked-list, the slow pointer is the node
### Solution
``` 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for _ in range(n):
            cur = cur.next

        # edge case
        if cur == None:
            return head.next

        # slow pointer
        slow = head
        while cur.next != None:
            cur = cur.next
            slow = slow.next
            
        
        slow.next = slow.next.next

        return head
'''
1  2 3 4 5 n=2
cur  1 -> 2 -> 3 -> 4 -> 5 -> None
slow 1 -> 2 -> 3 ->   -> 5
'''
```

## 206 Reverse Linked List
### Question
Given the `head` of a singly linked list, reverse the list, and return the reversed list.
### Notes
- [Reference](https://www.youtube.com/watch?v=G0_I-ZF0S38)
- save the next node before change the pointer
- return `pre`  
    ![](/Top-Interview-Easy/image/206.png)  
- 
### Solution
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            new = cur.next
            cur.next = pre
            pre = cur
            cur = new
        return pre
```


## 21 Merge Two Sorted Lists
### Question
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
### Notes
- Use `dummy` to create new linked list and `tail` to loop through
- whitch node is small, point to it and update it
- Edge case: one linked list have nodes left
- update `tail`
### Solution
```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Edge case
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next
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
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        l, r = 0, len(vals)-1
        while l <= r:
            if vals[l] != vals[r]:
                return False
            l += 1
            r -= 1
        return True
```

## 141 Linked List Cycle
### Question
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
### Notes
- `dictionary` or `set`: store node! can do this ! it is easy, check if key exists
- Two pointer: it is math problom, if it has a circle, fast will meet slow afer `(n - pos`)` times move
### Solution
set or dictionary: space, time O(n)
```
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        cur = head
        while cur:
            if cur in node_set:
                return True
            node_set.add(cur)
            cur = cur.next
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



