def mirror(data: list) -> list:
    data1 = sorted(data)
    data2 = []
    for i in range(1,len(data1)):
        data2.append(data1[len(data1)-1-i])
    return data1+data2



