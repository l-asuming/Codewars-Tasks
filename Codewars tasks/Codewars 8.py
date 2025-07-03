def substring_test(s1,s2):
    s11 = s1.lower()
    s22 = s2.lower()


    for i in range(len(s11)-1):
        for j in range(len(s22)-1):
            if s11[i].lower()==s22[j] and s11[i+1]==s22[j+1]:
                return True
             
    return False

   
