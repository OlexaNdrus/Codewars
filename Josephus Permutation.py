def josephus(items,k):
    res=[]
    counter=k
    while items:
        while k>len(items):
            k-=len(items)
        res.append(items[k-1])
        del items[k-1]
        k+=counter-1
    return res

print(josephus([1,2,3,4,5,6,7,8,9,10],2))