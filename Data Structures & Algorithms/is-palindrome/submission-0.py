class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        Sreversed = s[::-1]
        return Sreversed == s