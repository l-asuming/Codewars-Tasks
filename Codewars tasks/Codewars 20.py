import math

def divisor_finder(n):
    divisors = []
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
    for divisor in divisors:
        if n//divisor not in divisors:
            divisors.append(n//divisor)
    return sorted(divisors)

def find_min_num(num_div):
    i = 1
    while len(divisor_finder(i)) != num_div:
        i += 1
    return i



