def iq_test(numbers):
    helper=[True if int(i)%2==0 else False for i in numbers.split(' ')]
    if helper.count(True)==1:
        return helper.index(True)+1
    else:
        return helper.index(False)+1

print(iq_test('30 26 10 43 38 6 32 42 22 6 42 44 4 16 30 14 36 28 6 0 50 24 18 8 50 18 50 38 28 8 6 48 4 2 0 2 28'))