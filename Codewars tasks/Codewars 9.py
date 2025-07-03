import math
def compare_powers(n1,n2):
    if (n1[1]*math.log(n1[0])) > (n2[1]*math.log(n2[0])):
        return -1
    if (n1[1]*math.log(n1[0])) == (n2[1]*math.log(n2[0])):
        return 0
    else:
        return 1