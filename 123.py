from itertools import combinations

number='123'
b='8901'

starter=int(number[0])
# for i in range(1, len(number)):
#     starter = str(starter+1)[-1]
#     if starter == int(number[i]):
#         continue

if '0' in number and number[-1]!='0':
    print(number+'123')
for i in range(2):
    if all(True if int(str(starter+i)[-1]) == int(number[i]) else False for i in range(1, len(number))):
        print(number)
    starter=-starter

for i in range(int(len(number)//2)):
    if number[i]==number[-(i+1)]:
        print(number[i])


