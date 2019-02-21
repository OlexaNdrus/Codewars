def trailing_zeros(n,base):
    new_num=0
    for i,j in enumerate(reversed(str(n))):
        print(i,j)
        new_num+=int(j)*(base**i)
    counter=0
    while new_num/5>0:
        new_num //= 5
        counter+=new_num
    return counter

print(trailing_zeros(7,2))