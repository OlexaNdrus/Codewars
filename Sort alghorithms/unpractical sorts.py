import time
from random import shuffle, sample, randint


def Bogosort(array):
    while True:
        array = sample(array, ln)
        if array == sorted(array):
            return array

def Stooge_sort(array):
    while True:
        randi1 = randint(0,len(array)-1)
        randi2 = randint(randi1, len(array)-1)
        if array[randi1]>array[randi2]:
            array[randi1],array[randi2]=array[randi2],array[randi1]
        if array==sorted(array):
            return array

ln =1000
array = [randint(0, 1000) for i in range(ln)]

# start = time.time()
# for i in range(1):
#     if Bogosort(sample(array, ln)):
#         pass
# print((time.time() - start) / 100)

start = time.time()
for i in range(1):
    if Stooge_sort(sample(array, ln)):
        pass
print((time.time() - start) / 1)
