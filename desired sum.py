def calculate_years(principal, interest, tax, desired):
    period=0
    while principal<desired:
        principal+=principal*interest*(1-tax)
        period+=1
    return period

print(calculate_years(1000, 0.05, 0.18, 1100))