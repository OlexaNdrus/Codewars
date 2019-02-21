def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

seq=[]
for i in range(int(input())):
    seq.append(int(input()))
print(find_it(seq))
