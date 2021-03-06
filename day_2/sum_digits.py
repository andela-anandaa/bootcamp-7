
def sum_digits_recursion(A):
    '''
    Takes a list A, and returns
    the sum of all the digits in the
    list e.g. [10, 30, 45] should return
    1 + 0 + 3 + 0 + 4 + 5 = 13
    '''
    def sub(n):
        if n < 10:
            return n
        return sub(n % 10) + sub(n / 10)

    total = 0
    for i in A:
        total += sub(i)

    return total

# test your code

print sum_digits([10, 30, 45])

def sum_digits(A):
    total = 0
    for x in "".join([str(i) for i in a]):
        total += int(x)

    return total
