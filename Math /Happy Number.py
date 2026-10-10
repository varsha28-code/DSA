=======================Approach 1: Set (cycle detection)

class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True




===================Approach 2: Floyd's cycle detection

class Solution(object):
    def isHappy(self, n):
        def next_num(x):
            total = 0

            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10

            return total

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1




