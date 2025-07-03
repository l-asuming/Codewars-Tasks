def find_uniq(arr):
    k = len(arr)
    for i in range(0,k-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
        elif arr[k-1] != arr[k-2] and arr[k-1] != arr[k-3]:
            return arr[k-1]
    
         
print(find_uniq([ 0, 0, 0, 0, 0.55 ]))