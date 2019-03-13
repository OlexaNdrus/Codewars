from random import randint,sample
import time

def silly_sort(array):
    while True:
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        if all(array[i]<=array[i+1] for i in range(len(array)-1)):
            return array

def bubble_sort(array):
    alpha = 1
    while alpha!=len(array):
        for i in range(len(array)-alpha):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        alpha+=1
    return array

def shake_sort(array):
    alpha,beta=1,1
    while alpha+beta!=len(array):
        for i in range(len(array)-alpha):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        for i in range(len(array) - alpha,beta,-1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        alpha += 1
        beta += 1
    return array

def even_odd_sort(array):
    counter=1
    while True:
        if counter%2==0:
            start=1
        else:
            start=0
        for i in range(start,len(array)-1,2):
            if array[i]>array[i+1]:
                    array[i],array[i+1]=array[i+1],array[i]
        counter+=1
        if all(array[i] <= array[i + 1] for i in range(len(array) - 1)):
            return array

def comb_sort(array):
    step=(len(array)*10//13)
    while round(step)>=1:
        for i in range(0,len(array)-round(step)):
            if array[i]>array[i+round(step)]:
                array[i], array[i+round(step)] = array[i+round(step)], array[i]
        step=(step*10//13)
    return array

ln=1000
array=[randint(0,1000) for i in range(ln)]

print(sample(array,ln))

start = time.time()
for i in range(100):
    if silly_sort(sample(array,ln)):
        pass
print((time.time()-start)/100)

start = time.time()
for i in range(100):
    if bubble_sort(sample(array,ln)):
        pass
print((time.time()-start)/100)

start = time.time()
for i in range(100):
    if shake_sort(sample(array,ln)):
        pass
print((time.time()-start)/100)

start = time.time()
for i in range(100):
    if even_odd_sort(sample(array,ln)):
        pass
print((time.time()-start)/100)

start = time.time()
for i in range(100):
    if comb_sort(sample(array,ln)):
        pass
print((time.time()-start)/100)