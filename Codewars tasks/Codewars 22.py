def trace(matrix):
    trace_entries = []
    n = len(matrix)

    if matrix == []:
        return None
    
    for i in range(n):
        if n != len(matrix[i]):
            return None
        else: 
            trace_entries.append(matrix[i][i])
    
    return sum(trace_entries)
    
print(trace([]))

