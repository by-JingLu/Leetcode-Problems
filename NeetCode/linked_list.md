## 876 Middle of the Linked List
### Notes
- two pointer
- condition should be desided from odd and even
### Solution
```
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
```

## 2095 Delete the Middle Node of a Linked List
### Notes
- Use `dummy` to handle edge case
### Solution
```
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next
```
```
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next

        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return dummy.next
```

## 143 Reorder List
### Notes
- Use extra space
- Reverse the second half and merge two half: based on 21 and 2095
### Solution
Use extra space
```
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes_list = []
        while head:
            nodes_list.append(head)
            head = head.next

        left = 0
        right = len(nodes_list) - 1
        while left < right:
            nodes_list[left].next = nodes_list[right]
            left += 1
            nodes_list[right].next = nodes_list[left]
            right -= 1
            
        nodes_list[left].next = None
        return head
```

## 23 Merge k Sorted Lists
### Notes
- Binary merge based on merge two lists: time O(nlogK)
- Use new list to save merged list, when `len(lists) == odd`, save the last item -> renew `lists = new list`
### Solution
```
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge_two(list1, list2):
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

        while len(lists) > 1:
            mergelist = []
            n = len(lists)
            i = 0
            j = 1
            while j < n:
                l1 = lists[i]
                l2 = lists[j]
                mergelist.append(merge_two(l1, l2))
                i += 2
                j += 2
            if n % 2 != 0:
                mergelist.append(lists[-1])
            lists = mergelist

        return lists[0]
```