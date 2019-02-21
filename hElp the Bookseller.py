def stock_list(listOfArt, listOfCat):
    if not (listOfCat or listOfArt):
        return ''
    library={i:0 for i in listOfCat}
    for i in listOfArt:
        for j in listOfCat:
            if i.startswith(j):
                library[j]+=int(i.split(' ')[1])
    return ' - '.join(f'({i[0]} : {i[1]})' for i in library.items())

import time
start_time = time.time()

print(stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600","CDXE 500","CDXE 500","CDXE 500"],["A", "B"]))
print("--- %s seconds ---" % (time.time() - start_time))