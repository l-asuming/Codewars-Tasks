def max_product(lst, n_largest_elements):
    list_of_large = []
    product = 1
    i = 1
    
    while i <= n_largest_elements:
        list_of_large.append(max(lst))
        lst.remove(max(lst))
        i += 1

    for j in range(n_largest_elements):
        product = product*list_of_large[j]

    return product

    



print(max_product([8,6,4,6], 3))