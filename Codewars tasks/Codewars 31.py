def variance(numbers):
    
    population = len(numbers) 
    mean = sum(numbers)/population
    squares = 0
    
    for i in numbers:
        squares += (i-mean)**2
    
    return squares/population
    
    