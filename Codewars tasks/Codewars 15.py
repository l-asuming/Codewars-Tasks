import math
def isprime1(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for m in range(1,math.ceil((math.isqrt(n))/2)):
        if n % ((2*m)+1) == 0:
            return False
    return True

def minimum_number(numbers):
    sum_of_numbers = sum(numbers)
    i = sum_of_numbers 
    while i >= sum_of_numbers:
        if isprime1(i):
            break
        else:
            i += 1
    return i - sum_of_numbers
