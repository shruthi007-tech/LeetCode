# 345. Reverse Vowels of a String

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/reverse-vowels-of-a-string/

**Topics:** Two Pointers, String

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

**Constraints:**

- `1 <= s.length <= 3 * 10^5`
- `s` consist of **printable ASCII** characters.

## Solution (python3)

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= "aeiouAEIOU"
        s=list(s)
        left=0
        right=len(s)-1

        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[right],s[left]=s[left],s[right]

            left+=1
            right-=1
        return "".join(s)
        
```

*Runtime: 8 ms · Memory: 20.6 MB*

