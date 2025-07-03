import itertools
def create_two_sets_of_equal_sum(n):  
    set1 = []
    total_set = list(range(1,n+1))
    k = sum(total_set)/2

    if n*(n+1) % 4 != 0:
        return []

    for i in range(1,n):
        for subset in list(itertools.combinations(total_set,j)):
            if sum(subset) == k:
                set1 = set(subset)
                set2 = set(total_set) - set1
                return (set1),(set2)
                
    return []        
        
#failed as code runs too slow 


    

    

