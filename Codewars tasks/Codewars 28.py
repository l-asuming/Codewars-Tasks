from itertools import product

def rolldice_sum_prob(sum_, dice_amount):
    
    dice_values = [[1,2,3,4,5,6] for i in range(dice_amount)]
    combos = list(product(*dice_values))
    
    count = 0
    combo_number = len(combos)

    for i in range(combo_number):
        if sum(combos[i]) == sum_:
            count +=1
    
    return count/combo_number


print(rolldice_sum_prob(0,3))











        
    