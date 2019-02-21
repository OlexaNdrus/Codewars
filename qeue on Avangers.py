from itertools import combinations
def tickets(people):
    cost=25
    bank=[]
    min_bank = 0

    def recur(bank, min_people):
        try:
            if min_people - cost == 0:
                bank.append(min_people)
                people.remove(min_people)
                return True
            elif bank:
                for i in range(1,len(bank)+1):
                    for j in combinations(bank,i):
                        if (min_people-cost) == sum(j):
                            for l in j:
                                bank.remove(l)
                            bank.append(min_people)
                            people.remove(min_people)
                            return True
        except:
            return False

    for i in range(len(people)):
        min_people = min(people)
        if not recur(bank,min_people):
            return 'NO'
    return 'YES'


people=[]
for i in range(int(input())):
    people.append(int(input()))
print(tickets(people))