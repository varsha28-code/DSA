==================Approach 1: Convert to string

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]

===================Approach 2: Reverse half the number — recommended

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return x == rev or x == rev // 10
