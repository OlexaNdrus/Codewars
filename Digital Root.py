def digital_root(n):
    if len(str(n))>1:
        sum = 0
        for i in str(n):
            sum+=int(i)
        return digital_root(sum)
    return n

print(digital_root(12345))