def find_nb(m):
    counter=0
    step=1
    sqrt=int(m**0.5)
    if m%(sqrt) != 0:
        return -1
    while counter<sqrt:
        counter+=step
        step+=1
    if counter==sqrt:
        return step-1
    return -1


print(find_nb(2344157327302861457))
