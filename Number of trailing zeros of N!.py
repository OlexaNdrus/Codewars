import time
start_time = time.time()
def zeros(n):
    counter=0
    while n/5>0:
        n //= 5
        counter+=n
    return counter

print(zeros(100))

print("--- %s seconds ---" % (time.time() - start_time))