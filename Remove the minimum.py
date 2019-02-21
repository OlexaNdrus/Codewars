def remove_smallest(numbers):
    if numbers:
        numbers_li=numbers[:].remove(min(numbers))
        return numbers_li
    return numbers

print(remove_smallest([1,2,3,4,5]))