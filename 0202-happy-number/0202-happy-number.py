class Solution:
    def sum_squares(self, n: int) -> int:
        result = 0
        str_n = str(n)
        
        for digit in str_n:
            result += int(digit) ** 2
        
        return result

    def isHappy(self, n: int, checked_num: dict = None) -> bool:
        if checked_num is None:
            checked_num = {}
        
        if self.sum_squares(n) == 1:
            return True
        
        key = ''.join(sorted(str(n)))
        if key in checked_num:
            return False
        else:
            checked_num[key] = 1
        
        return self.isHappy(self.sum_squares(n), checked_num)
