import math

class Solution:
    def sum_squares(self, n: int) -> int:
        result = 0
        str_n = str(n)
        digits = len(str_n)
        
        for i in range(digits):
            result += int(math.pow(int(str_n[i]), 2))
        
        return result

    def isHappy(self, n: int, checked_num: dict = {}) -> bool:
        if self.sum_squares(n) == 1:
            return True
        
        key = ''.join(sorted(str(n)))
        if key in checked_num:
            return False
        else:
            checked_num[key] = 1
        
        return self.isHappy(self.sum_squares(n), checked_num)
