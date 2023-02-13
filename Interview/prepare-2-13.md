# Array -> mutable
##### 26 Remove Duplicates from Sorted Array:  
- sorted -> two pointer  
##### 283 Move Zeroes:  
- two pointer, same as 26
##### 217 Contains Duplicate:
- member check: `set` `set.add()` or `dictionary`
- `list` will cause time limited exceeded
##### 1 Two Sum
- solution1: sorted the array, then use two pointer
- solution2: go through item one by one as the first num, check the left items if `item == target - num`
##### 189 Rotate Array
- pay attention to the correct `k = k % len(nums)`
- rotate whloe -> rotate first k elements -> rotate rest n-k elements
##### 48 Rotate Image
- rotate all rows -> exchange `matrix[i][j]` and `matrix[j][i]` (`i < j` or `i > j`, not exchange back)
##### 136 Single Number
- first intuitively way: use list, `list.append()` and `list.remove()`. In worst situation `[4,3,2,1,4,3,2], time: O(n^2), space: O(n)
- second way: sorted the list first, check `nums[i]` and `nums[i+1]`, time: O(nlogn), space: O(1)
- third way: math, `2*sum[every num] - sum[list]`, time: O(n), space: O(n)
##### 350 Intersection of Two Arrays II (Not)
- understand the intersection: elements contains both in to arrays
- sorted the arrays first, then use two pointer
- can't use `set` because elements can duplicate which is not accepted by set
##### 66 Plus one (Not Recursion)
- list -> string -> int -> plus one -> string -> list
- recursion: basic case, recusive case
##### 36 Valid Sudoku
- Clarify the `stride = 3`
- Time complexity: go through the board 3 times, if `board=n`, the time comlexity O(3n) -> O(n)

# Stack
##### 20 Valid Parentheses
- use satck or use dictionary and stack
- if left, add to stack; else, pop the stack. if stack is empty or `stack[-1]` is not the pair, return `Flase`
##### 682 Baseball Game
- clarify the edge case: `+` not have two previous score
- double or add the previous score not mean pop them!
##### 155 Min Stack
- use list as stack, so use fuction `min(stack)` get the minimum item in syack

# String -> immutable
##### 5 Longest Palindromic Substring
- check odd and even substring separatly.
- compare with exsiting substring's length and update substring
##### 647 Palindromic Substrings
- same as 5, just count the num
##### 

# Linked-list

# Binary Search

# Sorting and Searching

# Dynamic Programming and Recursion

# Tree

# Graph




