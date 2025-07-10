from datetime import datetime

def am_pm_to_minutes(time_str: str) -> int:
    time_obj = datetime.strptime(time_str.strip(), "%I:%M %p")
    return time_obj.hour * 60 + time_obj.minute

def catch_the_bus(bus_times, boy_times):

    a = am_pm_to_minutes(bus_times[0])
    b = am_pm_to_minutes(bus_times[1])
    c = am_pm_to_minutes(boy_times[0])
    d = am_pm_to_minutes(boy_times[1])

    vals = []

    for i in range(a,b+1):
        vals.append(d-i)
    
    sum_ = sum(vals)

    if sum_ < 0:
        return 0
    elif sum_>(b-a+1)*(d-c+1):
        return 100
    else:
        return sum_/(b-a+1)*(d-c+1)
    

    
    

    




print(catch_the_bus(("4:53 PM", "5:00 PM"),   ("4:47 PM", "4:55 PM")))