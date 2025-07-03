def tram(stops, descending, onboarding):
    number_of_passengers = []
    number_of_passengers.append(onboarding[0])
    i = 0
    while i < stops-1:
        number_of_passengers.append(number_of_passengers[i]-descending[i+1]+onboarding[i+1])
        i += 1
    return max(number_of_passengers)

    