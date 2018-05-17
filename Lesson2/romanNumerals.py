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
        subtractions = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        for sub in subtractions:
            sub_tokens = s.split(sub)
            if len(sub_tokens) > 1:
                s = s.replace(sub, '')
                num += subtractions[sub]

        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
       
        for r in romans:
            tokens = s.split(r)
            l = len(tokens)
            if l > 1:
                num += (l-1)*romans[r]
        
        return num


s = 'J'
ans = romanToInt(s)
print('Roman: {roman:1} \nAnswer: {integer:1}'.format(roman=s, integer=ans))

