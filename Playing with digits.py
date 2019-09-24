def dig_pow(n, p):
    num,pow=0,p
    for dig in str(n):
        num+=int(dig)**pow
        pow+=1
    return num/n if num%n==0 else -1

print(dig_pow(46288,  3))