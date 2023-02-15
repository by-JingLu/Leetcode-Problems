# Array -> mutable
#### 26 Remove Duplicates from Sorted Array:  
- already sorted -> two pointer  
#### 283 Move Zeroes:  
- two pointer, same as 26
#### 217 Contains Duplicate:
- member check: `set` `set.add()` or `dictionary`
- `list` will cause time limited exceeded
#### 1 Two Sum
- solution1: sorted the array, then use two pointer
- solution2: go through item one by one as the first num, check the left items if `item == target - num`
#### 189 Rotate Array
- pay attention to the correct `k = k % len(nums)`
- rotate whloe -> rotate first k elements -> rotate rest n-k elements
#### 48 Rotate Image
- rotate all rows -> exchange `matrix[i][j]` and `matrix[j][i]` (`i < j` or `i > j`, not exchange back)
#### 136 Single Number
- first intuitively way: use list, `list.append()` and `list.remove()`. In worst situation `[4,3,2,1,4,3,2], time: O(n^2), space: O(n)
- second way: sorted the list first, check `nums[i]` and `nums[i+1]`, time: O(nlogn), space: O(1)
- third way: math, `2*sum[every num] - sum[list]`, time: O(n), space: O(n)
#### 350 Intersection of Two Arrays II (Not)
- understand the intersection: elements contains both in to arrays
- sorted the arrays first, then use two pointer
- can't use `set` because elements can duplicate which is not accepted by set
#### 66 Plus one (Not Recursion)
- list -> string -> int -> plus one -> string -> list
- recursion: basic case, recusive case
#### 36 Valid Sudoku
- Clarify the `stride = 3`
- Time complexity: go through the board 3 times, if `board=n`, the time comlexity O(3n) -> O(n)

# Stack
#### 20 Valid Parentheses
- use satck or use dictionary and stack
- if left, add to stack; else, pop the stack. if stack is empty or `stack[-1]` is not the pair, return `Flase`
#### 682 Baseball Game
- clarify the edge case: `+` not have two previous score
- double or add the previous score not mean pop them!
#### 155 Min Stack
- use list as stack, so use fuction `min(stack)` get the minimum item in stack

# String -> immutable
#### 5 Longest Palindromic Substring
- solution1: list all substring then check if it is palindromic. O(n<sup>3</sup>)
- check odd and even substring separatly. O(n<sup>2</sup>)
- compare with exsiting substring's length and update substring
#### 647 Palindromic Substrings
- same as 5, just count the num
#### 7 Reverse Integer
- int -> string -> list -> reverse -> string -> int
- talk about positive and negative number separately
#### 387 First Unique Character in a String
- set: check existing and rest part of the string O(n*n!)
- dictionaty: with the letter as the key and the count of the letter as the value. O(3n)
#### 242 Valid Anagram
- sorted: more intuitivelly, then check equal or not. O(2nlogn) -> O(nlogn)
- list: check the letter then remove. O(2n) -> O(n)
#### 125 Valid Palindrome
- two pointer, escape `not .isalnum()`
#### 8 String to Integer (atoi)
- hard to understand all cases
#### 28 Find the Index of the First Occurrence in a String
- fix size sliding window
- check every fix size substring
- if using slicing, the right boader can be `len(s)`
#### 14 Longest Common Prefix
- handle the edge case: if `''`  in array, just return
- check every single letter, if it is common, add to prefix
#### 3 Longest Substring Without Repeating Characters
- two pointers  O(n!)
- two pointers -> sliding window O(n)

# Linked-list
1. the condition always be `while node and node.next:` if want to get `node.next.next`
2. `dummy = ListNode(0, head)` always be used to remove node in original linked-list
3. when need to delete middle node, check odd and even to decide the condition
#### 203 Remove Linked List Elements
- use a `dummy` linked list to handle the situation: first element alse need to remove
- if use `cur.next.next`, should give the condition: `cur.next != None`
#### 19 Remove Nth Node From End of List
- edge case: nth Node is the first node, `fast=None`
- fast pointer reached th last node of the linked-list, the slow pointer is the node before the node should be moved
#### 2095 Delete the Middle Node of a Linked List
- we need to stop the node before the middle node to remove it
- so we use `dummy` and change the condition
#### 21 Merge Two Sorted Lists
- use `dummy` and `tail`
- whitch node is small, point to it and update it
- update tail
#### 206 Reverse Linked List
- save the next node before change the pointer
- return `pre`  
![](/Interview/p1.png)  
- understand recursive solution: problem -> sub-problem
```
1 -> 2 -> 3
     2 -> 3
          3

```
#### 234 Palindrome Linked List
- get value of each node as list, check the list
#### 876 Middle of the Linked List
- two pointer
#### 141 Linked List Cycle
- solution1: use `set` store `node`! can do this!
- solution2: two pointer `fast` and `slow`; in the while loop, update poniter first then compare, because  at the beginner `fast = slow`

# Binary Search
1. non-decreasing/increasing/ascending array/numbers
2. three pointers: `l`, `r`, `mid=(l+r)//2`
3. condition `l <= r`
4. update `l` or `r`, don't forget `+1` or `-1`
#### 704 Binary Search
- baisc binary search
#### 278 First Bad Version
- if isNotBadVersion, just let `l=mid+1`, because the target must appear in right part
- if isNotBadVersion(mid) and isNotBadVersion(mid-1), let `r=mid-1`, because first must appear in left part
#### 35 Search Insert Position
- if target in the given list, it is a nornmal binary search
- if not, we can use two edge exambles to decide final return: `[1,2,3], 0, 4`
#### 69 Sqrt(x)
- same as 35, need to decide the final output after bianry search loop
#### 34 Find First and Last Position of Element in Sorted Array
- don't just focus on the binary search, find out the other way
- solution1: from left to right and from right to left go through the array separatly. O(2n) -> O(n)

# Sorting and Searching
#### 75 Sort Colors
- solution1: go through the array, save the count of each num, then loop through again to change the array time: O(2n), space: O(1)
- solution2: [bubble sort O(n<sup>2</sup>)](/Interview/75-bubblesort.py)

#### 88 Merge Sorted Array
- intuitively solution: merge -> sort(bubble sort) O((m+n)<sup>2</sup> + n)
- use two pointer: if the problem change to `nums1=[1,2,3]` `nums2=[1,2,5]` and merge them, it is much easier.
- based on that, we just need to shift the pointers from end to start and add a new pointer states the index of final array

# Dynamic Programming and Recursion


# Tree

# Graph




