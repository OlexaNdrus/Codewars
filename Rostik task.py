import timeit
from typing import List

setup="""
d = [1, 15, 3]
e = [0, 5, 20]


def unite_two_list_and_sort(list1, list2):

    n = list1 + list2
    for i in range(len(n)-1, 0, -1):
        for x in range(i):
            if n[x] > n[x+1]:
                n[x], n[x+1] = n[x+1], n[x]

    return n

"""
time = timeit.Timer(stmt='unite_two_list_and_sort(d, e)',setup=setup)
print(time.timeit(1000000))