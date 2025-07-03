def find_all(array, n):
    index_list = []
    for i in range(len(array)):
        if array[i]==n:
            index_list.append(i)
    return index_list


