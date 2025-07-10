def remove_duplicate_ids(obj):
   
    keys = sorted([int(i) for i in list(obj.keys())])
    keys = [str(i) for i in keys]
    
    for j in keys:
        obj[j] = list(dict.fromkeys(obj[j]))
    
    obj_1 = {j:obj[j] for j in keys}

    obj_1_values = (list(obj_1.values()))

    k = len(obj_1_values)-1

    while k>0:
        for l in range(k):
            if len(set(obj_1_values[l]).intersection(set(obj_1_values[k])))>0:
                for m in set(obj_1_values[l]).intersection(set(obj_1_values[k])):
                    obj_1_values[l].remove(m)
        k -= 1  

    obj_2 = {n:obj_1_values[keys.index(n)] for n in keys}
    
    return obj_2

