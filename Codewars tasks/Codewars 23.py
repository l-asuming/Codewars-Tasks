def moment_of_time_in_space(moment):
    
    num_of_characters = 8
    i = 0

    time_list = []

    while i < num_of_characters:
        try: 
            time_list.append(int(list(moment)[i]))
            i += 1
        except:
            i += 1
    
    time_list = list(filter(lambda k:k!= 0,time_list))
    time = sum(time_list)
    space = num_of_characters - len(time_list)

    return[time<space, time == space, time>space]

print(moment_of_time_in_space("01:00 pm"))

