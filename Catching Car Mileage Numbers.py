def is_interesting(number, awesome_phrases):
    interest = 2
    number = str(number)
    for i in range(3):
        if 99 < int(number) < 1000000000:
            if number.count('0') == len(number) - 1:
                return interest
            if number.count(number[0]) == len(number):
                return interest
            if int(number) in awesome_phrases:
                return interest

            if all(True if number[i] == number[-(i + 1)] else False for i in range(int(len(number) // 2))):
                return interest

            starter = int(number[0])
            for i in range(2):
                if '0' in number:
                    if number[-1] != '0':
                        continue
                if all(True if int(str(starter + i)[-1]) == int(number[i]) else False for i in range(1, len(number))):
                    return interest
                starter = -starter
        interest = 1
        number = str(int(number) + 1)
    return 0


print(is_interesting(1111,[]))