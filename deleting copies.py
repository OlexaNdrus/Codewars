
def delete_nth(order,max_e):
    new_order = list(reversed(order))
    for i in order:
        if new_order.count(i)>max_e:
            for j in range(new_order.count(i)>max_e):
                new_order.remove(i)
    return new_order[::-1]

order=[]
for i in range(int(input())):
    order.append(int(input()))
print(delete_nth(order,int(input())))