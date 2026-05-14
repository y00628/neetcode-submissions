class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        for i in range(len(s) // 2):
            left, right = i, len(s)-1-i

            if s[left] != s[right]:
                return False
        
        return True