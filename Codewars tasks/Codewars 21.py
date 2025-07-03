def count_binary(s1, s2):
    count = 0
    k = len(s1)
    r = len(s2)
    for i in range(0,r-k):
        if s2[i:k+i:] == s1:
            count += 1
    return count





