## 344. Reverse String
### Question
Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array `in-place` with `O(1)` extra memory.
### Solution
My solution:
``` 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

```
Others' solution:
```
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): 
            s[i], s[-i-1] = s[-i-1], s[i]
```
### Notes
- Items can be changed in array and list, but not in string.
- While the two pointers are "increasing" in the same speed, we can use one `i` to  represent `left` and `right`.

## 557. Reverse Words in a String III
### Question
Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
### Solution
``` 
class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        
        for i in range(len(words_list)):
            word = list(words_list[i])
            
            left = 0
            right = len(word) - 1
            while left <= right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            words_list[i] = "".join(word)
            i += 1
        
        return " ".join(words_list)
```
### Notes
- `s.split()` can make sentence to words or split string with given attribute; `list(s)` make whole string to single character.
```
>>> s = "Hello word"
>>> print(s.split())
['Hello', 'word']
>>> print(list(s))
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'd']
```
