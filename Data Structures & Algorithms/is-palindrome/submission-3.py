class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        
        return s_cleaned == s_cleaned[::-1]