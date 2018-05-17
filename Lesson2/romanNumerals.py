"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Roman numerals are represented using seven different symbols:

===================
-- I -- | --- 1 - |
-- V -- | --- 5 - |
-- X -- | -- 10 - |
-- L -- | -- 50 - |
-- C -- | - 100 - |
-- D -- | - 500 - |
-- M -- |  1000 - |
===================

Examples:

2: II (I + I)
12: XII (X + II)
27: XXVII (XX + V + II)

Usually Roman Numerals have an addition rule (see above), however there are 6 instances when 
subtraction is used:

IV: 4 (V - I)
IX: 9 (X - I)
XL: 40 (L - X)
XC: 90 (C - X)
CD: 400 (D - C)
CM: 900 (M - C)

"""

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        
        num = 0

        # First check for subtractions
        sub_romans = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        sub_nums = [4, 9, 40, 90, 400, 900]
        
        for sub_r, sub_n in zip(sub_romans, sub_nums):
            sub_tokens = s.split(sub_r)
            if len(sub_tokens) > 1:
                s = s.replace(sub_r, '')
                num += sub_n

        romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        nums = [1, 5, 10, 50, 100, 500, 1000]

        for r, n in zip(romans, nums):
            tokens = s.split(r)
            print(tokens)
            l = len(tokens)
            if l > 1:
                num += (l-1)*n
        
        return num




            

            
            

s = 'III'
ans = romanToInt(s)
print(ans)

