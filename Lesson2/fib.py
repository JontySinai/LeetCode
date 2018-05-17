"""
Fibonacci Sequence
"""

def fib_print(n):
    """usage
    for n in range(1,11):
        fib_print(n)
    """
    a, b, = 0, 1

    for _ in range(n):
        a, b = b, a + b # note must do simultaneous update!

    print('{ind:3}: {fib:3}'.format(ind=n,fib=a))


def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)



def fib_generator():
    """ usage
    for index, fibonacci_number in zip(range(1,11), fib_generator()):
        print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b



