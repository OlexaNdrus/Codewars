import time
from math import ceil
def list_squared(m, n):
    res =[]
    if m <= 1:
        res.append([1, 1])
    for j in range(m ,n+1):
        step = 2 if j % 2 else 1
        summer=0
        for i in range(1, ceil(j**0.5),step):
            if j % i == 0 :
                summer+=i*i
                summer+=int(j/i)**2
        if (summer**0.5).is_integer() and summer!=0:
            res.append([j, summer])

    return res
start_time = time.time()

print(list_squared(0,250000))
print("--- %s seconds ---" % (time.time() - start_time))



