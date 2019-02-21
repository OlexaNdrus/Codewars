import re
def count_smileys(arr):
    counter=0
    pattern=re.compile(r'([;:])([-~])*([)D])')
    for i in arr:
        if re.search(pattern, i):
            counter+=1
    return counter

print(count_smileys([':D',':~)',';~D',':)']))