def bonus_time(salary, bonus = True):
    if bonus:
        new_salary = f"${salary * 10}"
    else:
        new_salary = f"${salary}"
    return new_salary

print(bonus_time(100, True))