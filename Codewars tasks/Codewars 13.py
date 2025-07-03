def array_madness(a,b):
    sum_a = 0
    sum_b = 0
    for i in range(len(a)):
        sum_a += (a[i])**2
    for j in range(len(b)):
        sum_b += (b[j])**3 
    if sum_a > sum_b:
        return True
   
    
        