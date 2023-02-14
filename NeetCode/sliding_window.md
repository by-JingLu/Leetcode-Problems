## 3 Longest Substring Without Repeating Characters
### Notes
- worst case: 'abcdefgg'
- solution1: just use two pointers O(n!)
- solution2: shrinking window size by 1 when meet repeat O(2n)
  ![](/NeetCode/p1.png)
- solution3: shrinking window until not have repeat O(n)
  ![](/NeetCode/p2.png)
  ![](/NeetCode/p3.png)
### Solution
1
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        sub = set()
        res = 0
        i = 0
        j = i

        while j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                j += 1
            else:
                res = max(res, j - i)
                sub = set()
                i += 1
                j = i
        
        res = max(res, j - i)
        return res

```
2
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        sub = set()
        res = 0
        i = 0
        j = i

        while j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                j += 1
            else:
                res = max(res, j - i)
                sub.remove(s[i])
                i += 1

        res = max(res, j - i)
            
        return res
```
3
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res
```
