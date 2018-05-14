"""
Given a 32-bit signed integer, reverse digits of an integer.

Examples:
```python
reverse(123)
>>> 321

reverse(-123)
>>> -321

reverse(120)
>>> 21
```
"""

def reverse(x):
        """
        :type x: int
        :rtype: int

        Implements string reversal
        """

        x_str = str(abs(x))
        
        while len(x_str) > 1: # remove zeros at end
            if x_str[-1] == '0':
                x_str = x_str[:-1]
                continue
            break

        reverse = int(x_str[::-1])
        

        if x < 0:
            reverse = -reverse

        if reverse > -2**31 and reverse < 2**31 - 1:
            print(reverse)
        else:
            print(0)

def reverse_modulo(x):
    """
    :type x: int
    :rtype: int

    Implements modulo arithmetic to reverse the string. Offers no speed benefit to above ^^
    
    if x = 123

    reverse = 100*(x mod 10) + 10*(floor(x/10) mod 10) + 1*(floor(x/100) mod 10)
            = 100*(123 mod 10) + 10*(12 mod 10) + 1*(1 mod 10)
            = 100*(3) + 10*(2) + 1*(1)
            = 321

    """

    reverse = 0
    x_pos = abs(x)
    
    while x_pos != 0:
        reverse *= 10
        reverse += x_pos % 10
        x_pos = int(x_pos/10)

    if x < 0:
        reverse = -reverse
    
    if reverse > -2**31 and reverse < 2**31 - 1:
        print(reverse)
    else:
        print(0)


test = -1230000
test_long = 1534236469

reverse(test)