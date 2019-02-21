from math import ceil

def whoIsNext(names, r):
    if r<len(names):
       return names[r-1]
    step,counter=5,1
    while step*2+5<r:
        step=step*2+5
        counter+=1
    place= ceil((r-step)/2**counter)
    return names[place-1]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
r = 1
print(whoIsNext(names,r))