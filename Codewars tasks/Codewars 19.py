
def remov_nb(n):
    sum1 = n*(n+1)//2
    solutions = []
    for a in range(1,n+1):
        b = (sum1-a)//(a+1) 
        if a*b == sum1-a-b and 1<=b<=n:
            solutions.append((a,b))
            
    return solutions(250)
