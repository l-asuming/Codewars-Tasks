def get_min_avg_max(discard, data):

    arrays = [[] for i in range(len(data)+1)]

    for k in range(len(data)):
    
        data[k] = data[k][discard:len(data[k])-discard]

        arrays[k].append(min(data[k]))
        arrays[k].append(sum(data[k])/len(data[k]))
        arrays[k].append(max(data[k]))

    k = 0
    combined_data = []
    
    while k < len(data):
        combined_data += data[k]
        k += 1

    arrays[len(data)].append(min(combined_data))
    arrays[len(data)].append(sum(combined_data)/len(combined_data))
    arrays[len(data)].append(max(combined_data))

    return arrays
    
print(get_min_avg_max(2,[[800,1200,2100,4100,1300,700],[1000, 1500, 4500, 5000, 5800, 2000, 1500]]))

