"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""

def isPalindrome_string(x):
    """
    :type x: int
    :rtype: bool

    Simple but inefficient string method (although took <1min to write a solution)
    """
        
    x_str = str(x)
        
    x_reverse = x_str[::-1]
        
    if x_str == x_reverse:
        return True
    else:
        return False



def isPalindromeHalf(x):
    """
    :type x: int
    :rtype: bool

    This method reverses half the integer and comapres if the first half equals reverse(second half)
    """

    # time savers: negative ; check if last digit is zero when x != 0
    if (x < 0) or (x != 0 and x % 10 == 0):
        return False

    reversed_half = 0

    while (x > reversed_half): # we've reached halfway when we've removed more digits from x then what we've added to reversed_half
        reversed_half *=10
        reversed_half += x % 10 # last digit
        x //= 10 # remove last digit


    # At end of while loop for x=12321, reversed_half = 123, but x = 12.
    # We can easily remove the last digit if necessary using y//10

    if (x == reversed_half) or (x == reversed_half//10):
        return True
    else:
        return False



def isPalindrome(x):
    """
    :type x: int
    :rtype: bool

    Note: this method is SLOW

    This method requires no extra space but recursively compares the first and last digits of an integer.

    Consider x=122:

    x//100 = 1 # first digit
    x % 10 = 2 # last digit

    If not equal this will never be a palindrome.

    If equal (ie. x=121), then they will be the same. Drop the first and last digits and rinse and repeat.
    x = 121 => x' = 2
    x//1 = 2 # first digit
    x % 10 = 2 # last digit

    The first challenge is to get the correct divisor and update it. 
    The next challenge is to correctly drop the first and last digits.
    """

    if (x < 0): # requirements: negative integers can never be palindromes
        return False

    divisor = 1 # base case when 0 < x < 10

    while (x/divisor > 10): # we want the integer part of x/div to be 1 digit (ie < 10)
        divisor *= 10

    while (x != 0): # (x % 1)//10 = 0 when 0 < x < 10

        first = x // divisor
        last = x % 10 # note that 3 % 10 = 3

        # check first and last:
        if (first != last):
            return False

        # remove the last digit
        x = (x % divisor)//10 # 1221 % 1000 = 221 ; 221 // 10 = 22

        # two digits droped, so reduce divisor by a factor of 2
        divisor /= 100 # no need to worry if divisor < 1 since (y)//0.1 = 0.0

    return True
    

    test = 123
if isPalindromeHalf(test):
    print('Yes')
else:
    print('No')