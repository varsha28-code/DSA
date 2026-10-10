class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plusone=int("".join([str(d) for d in digits])) + 1
        return[int(d) for d in str(plusone)]
