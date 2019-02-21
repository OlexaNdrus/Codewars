from itertools import permutations

def permutation(shit):
    combo=[]
    string=''
    for i in shit:
        string+=i
    for i in permutations(string):
        print(i)
        combo.append(''.join(i))
    return combo

print(sorted(permutation('ab')))