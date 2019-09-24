def reverser(digit):
    result, multiplayer = 0, digit
    while multiplayer:
        result = result*10 + multiplayer % 10
        multiplayer //= 10
    return result

print(reverser(123))