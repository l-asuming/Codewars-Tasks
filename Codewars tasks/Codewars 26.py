def is_a_valid_message(message):
    
    index_of_ints = []
    message = list(message)
    message = [int(x) if x.isdigit() else x for x in message]

    if len(message)==0:
        return True
    
    for i in range(len(message)):
        if isinstance(message[i],int):
            index_of_ints.append(i)

    if index_of_ints[len(index_of_ints)-1] == len(message)-1:
        return False

    print(f"Initial index of ints is {index_of_ints}")
    print(f"Initial message is {message}")

    iteration = 0
   
    j = 0
    
    while j+1 < len(index_of_ints):
        if index_of_ints[j+1]-index_of_ints[j]==1:
            message[index_of_ints[j]:index_of_ints[j]+2] = [int("".join(map(str,[message[index_of_ints[j]],message[index_of_ints[j+1]]])))]
            index_of_ints.pop(j)
            index_of_ints = [x-1 if k>=j else x for k, x in enumerate(index_of_ints)]
            j += 1
            iteration +=1
            print(f"Iteration:{iteration}, index of ints is {index_of_ints}, message is {message}")
        else:
            j += 1
    
    for l in range(len(index_of_ints)-1):
        if index_of_ints[l+1]-index_of_ints[l]-1 != message[index_of_ints[l]]:
            return False
    if len(message)-index_of_ints[len(index_of_ints)-1]-1 != message[index_of_ints[len(index_of_ints)-1]]:
            return False
    
    return True

print(is_a_valid_message("3hey5hello2hi"))
       
           




