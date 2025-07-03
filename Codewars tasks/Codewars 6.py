def abbrev_name(name):
    capitalized_name = name.upper()
    for i in range(len(capitalized_name)):
        if capitalized_name[i].isspace() == True:
            print(f"{capitalized_name[0]}.{capitalized_name[i+1]}")




 

    