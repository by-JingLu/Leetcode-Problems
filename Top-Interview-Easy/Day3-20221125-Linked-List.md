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
### Notes
- 
### Solution
```
```

## 206 Reverse Linked List
### Question
Given the `head` of a singly linked list, reverse the list, and return the reversed list.
### Notes
- [Reference1](https://leetcode.wang/leetcode-203-Remove-Linked-List-Elements.html), [Reference2](https://leetcode.com/problems/reverse-linked-list/solutions/58170/classic-2-pointer-approach-with-linear-runtime-and-constant-space-in-python/?languageTags=python)
- Iteratiion and Recursion
### Solution
```
```
```
```


## 21 Merge Two Sorted Lists
### Question
### Notes
- 
### Solution
```
```


## 234 Palindrome Linked List
### Question
### Notes
- 
### Solution
```
```

## 141 Linked List Cycle
### Question
### Notes
- 
### Solution
```
```



